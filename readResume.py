import PyPDF2
import spacy
import tkinter as tk
from tkinter import filedialog
import re

nlp = spacy.load("en_core_web_sm")

def select_pdf_file():
    # Open a Tkinter file dialog to select a PDF file
    root = tk.Tk()
    root.withdraw()  # Hide the main tkinter window
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    return file_path

def extract_text_from_pdf(pdf_file):
    with open(pdf_file, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text

predefined_skills = [
    "python", "java", "javascript", "html", "css", "machine learning", "deep learning", 
    "data science", "flask", "django", "node.js", "react.js", "swift", "postgresql", 
    "sql", "c/c++", "linux", "git", "docker", "kubernetes", "pytorch", "spring boot", 
    "restful api", "agile", "tensorflow", "swiftui", "jupyter", "jenkins"
]

def clean_text(text):
    # Remove phone numbers and URLs
    text = re.sub(r'\|\s?\d{3}-\d{3}-\d{4}', '', text)  # Remove phone numbers
    text = re.sub(r'http[s]?://\S+', '', text)  # Remove URLs
    return text

def extract_skills(resume_text):
    # Clean the text to remove irrelevant parts like phone numbers and URLs
    resume_text = clean_text(resume_text)
    
    # Process the text with spaCy NLP model
    doc = nlp(resume_text)
    
    # List to store identified skills
    skills = []
    
    # Iterate through each token in the document and check if it's a skill
    for token in doc:
        # Add to skills list if the token is in the predefined skill list
        if token.text.lower() in predefined_skills:
            skills.append(token.text.lower())
    
    # Return unique skills (to remove duplicates)
    return list(set(skills))

def main():
    # Ask the user to select a PDF file
    print("Please select your resume (PDF file):")
    pdf_file = select_pdf_file()
    
    if pdf_file:
        # Extract text from the selected PDF
        resume_text = extract_text_from_pdf(pdf_file)
        detail = extract_skills(resume_text)
        print(detail)

if __name__ == "__main__":
    main()
    