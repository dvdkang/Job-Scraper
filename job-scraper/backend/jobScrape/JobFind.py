import requests
from bs4 import BeautifulSoup
from .nlp import extract_section
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import quote
from .openai import extract_skills
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import asyncio

# Define your chain once
template = """
description: {description}

Answer:
"""
model = OllamaLLM(model="llama3.2")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model


def extract_description(job_url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'}
    response = requests.get(job_url, headers)
    soup = BeautifulSoup(response.content, "html.parser")
    description_div = soup.find("div", class_="show-more-less-html__markup")
    
    return description_div.prettify() if description_div else "No description found"


def extract(role, location): 
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'}
    role = quote(role)
    loc = quote(location)
    url = f'https://www.linkedin.com/jobs/search?keywords={role}&location={loc}&geoId=&f_TPR=r86400&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def extract_job(item, chain):
    title = item.find(class_ = 'base-search-card__title').text.strip()
    company = item.find(class_ = 'base-search-card__subtitle').text.strip()
    location = item.find(class_ = 'job-search-card__location').text.strip()
    job_link = item.find('a', class_='base-card__full-link')['href']  # Extracts job URL
    description = extract_description(job_link)
    
    keywords = ['key', 'skills', 'qualifications', 'experience', 'you', 'requirements', 'who are you', 'you?']
    requirements = extract_section(description, keywords)
    if requirements == "No relevant sections found":
        cleaned_description = BeautifulSoup(description, 'html.parser').get_text(separator='\n')
        cleaned_description = " ".join(cleaned_description.split()[:700])
        requirements = extract_skills(cleaned_description, chain)

    return {
        'title': title,
        'company': company,
        'location': location, 
        'link': job_link,
        'requirements': requirements
    }

### Keeping this one as this one works
# def job_scrape_streaming(job_role="software engineer", location="United States", max_jobs=10):
#     soup = extract(job_role, location)
#     job_cards = soup.find_all('div', class_='job-search-card')
#     joblist = []
#     with ThreadPoolExecutor() as executor:
#         futures = {executor.submit(extract_job, card): i for i, card in enumerate(job_cards)}
        
#         for i, future in enumerate(as_completed(futures)):
#             job = future.result()
#             joblist.append(job)

#             progress = int((len(joblist) / len(futures)) * 100)
#             yield {"progress": progress}

#     yield {"done": True, "jobs": joblist}

### Testing so that I could improve the speed of using openai to summarize my descriptions
async def extract_async(job_card, loop, executor, chain):
    return await loop.run_in_executor(executor, extract_job, job_card, chain)

async def job_scrape_streaming(job_role="software engineer", location="United States", max_jobs=10):
    soup = extract(job_role, location)
    job_cards = soup.find_all('div', class_='job-search-card')[:max_jobs]
    joblist = []
    
    loop = asyncio.get_event_loop()
    executor = ThreadPoolExecutor()
    
    futures = [extract_async(card, loop, executor, chain) for card in job_cards]

    for i, future in enumerate(asyncio.as_completed(futures)):
        job = await future
        joblist.append(job)
        progress = int((len(joblist) / len(futures)) * 100)
        yield {"progress": progress}

    yield {"done": True, "jobs": joblist}