import spacy
from bs4 import BeautifulSoup, NavigableString

nlp = spacy.load("en_core_web_sm")

def extract_section(description, keywords):
    """Extracts sections based on context using BeautifulSoup and spaCy for NLP processing."""
    soup = BeautifulSoup(description, 'html.parser')
    
    # Find all <strong> tags (section headers)
    strong_tags = soup.find_all('strong')
    
    sections = []

    for tag in strong_tags:
        tag_text = tag.get_text(strip=True)
        
        if any(keyword.lower() in tag_text.lower() for keyword in keywords):
            current_section = [tag_text]  # Use markdown-style header
            
            # Traverse next siblings to capture content
            next_sibling = tag.next_sibling
            
            while next_sibling:
                if isinstance(next_sibling, NavigableString):  # Plain text
                    text = next_sibling.strip()
                    if text:
                        current_section.append(text)
                
                elif next_sibling.name == "br":  # Line break
                    current_section.append("\n")
                
                elif next_sibling.name in ["p", "div"]:  # Block elements
                    current_section.append(next_sibling.get_text(strip=True))
                
                elif next_sibling.name == "strong":  # Stop at next section header
                    break
                
                elif next_sibling.name == "ul":  # Handle lists
                    for li in next_sibling.find_all("li"):
                        current_section.append(f"- {li.get_text(strip=True)}")
                    break
                
                next_sibling = next_sibling.next_sibling

            sections.append("\n".join(current_section).strip())

    # NLP Processing with spaCy
    formatted_sections = []
    for section in sections:
        doc = nlp(section)
        formatted_text = "\n".join([sent.text.strip() for sent in doc.sents])
        formatted_sections.append(formatted_text)

    return "\n\n".join(formatted_sections) if formatted_sections else "No relevant sections found"