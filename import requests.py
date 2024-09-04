import re
import requests
from bs4 import BeautifulSoup
from transformers import pipeline

# Load a pre-trained transformer model for text classification (if needed)
content_classifier = pipeline("text-classification", model="distilbert-base-uncased", tokenizer="distilbert-base-uncased")

def clean_text(text):
    # Remove backslashes and excessive whitespace
    text = re.sub(r'\\+', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Remove markdown links
    text = re.sub(r'\[.*?\]\(.*?\)', '', text)
    
    return text

def extract_content(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find all div elements with class 'statement'
    statement_divs = soup.find_all('div', class_='statement')
    
    content_blocks = []
    
    for div in statement_divs:
        # Extract the outer HTML of the div
        outer_html = div.encode_contents().decode('utf-8')
        cleaned_content = clean_text(outer_html)
        content_blocks.append(cleaned_content)
    
    # Join all content blocks into a single string
    content = "\n".join(content_blocks)
    
    return content

def scrape_and_abstract_content(url):
    response = requests.get(url)
    cleaned_content = extract_content(response.content)
    
    # Define the structure of the final output
    path = url.split('/')[-2] + "_"
    title = BeautifulSoup(response.content, 'html.parser').title.string.strip()
    
    return {
        "path": path,
        "title": title,
        "content": cleaned_content
    }

# Example usage
urls = [
    "https://www.law.cornell.edu/supremecourt/text/24A78",  # Replace with actual URLs
    # Add more URLs as needed
]

results = []
for url in urls:
    data = scrape_and_abstract_content(url)
    results.append(data)

# Convert results to JSON
import json
json_output = json.dumps(results, indent=4)
print(json_output)
