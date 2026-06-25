import re
import requests
from ollama import chat
from bs4 import BeautifulSoup
from ollama import ChatResponse

# List of URLs
Url = [
    "C11-Adversarial-Robustness.md",
    "C12-Privacy.md",
    "C13-Monitoring-and-Logging.md",
    "C14-Human-Oversight.md",
]

BaseUrl = "https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-"

def extract_text_between_numbers(text):
    pattern = r'\d+(?:\.\d+)+'
    matches = list(re.finditer(pattern, text))
    results = []
    for i in range(len(matches) - 1):
        start = matches[i].end()
        end = matches[i + 1].start()
        between_text = text[start:end].strip()
        if between_text:
            results.append(between_text)
    return results

def fetch_html(url):
    response = requests.get(url)
    return response.text

def process_url(url, url_index):
    full_url = BaseUrl + url
    print(f"Processing URL: {full_url}")
    html_doc = fetch_html(full_url)
    soup = BeautifulSoup(html_doc, 'html.parser')
   
    auto_dir_paragraphs = soup.find_all('p', attrs={'dir': 'auto'})
    
    auto_heading_h1 = soup.find_all('h1', attrs= {'class': 'heading-element'})

    auto_heading_h2 = soup.find_all('h2', attrs= {'class': 'heading-element'})

    control_context = auto_heading_h1 + auto_dir_paragraphs + auto_heading_h2
        
    with open("control_context.txt", "w") as file:
        file.write(str(control_context))

    # Extract relevant table data
    scrape_result = soup.find_all("td", limit=75)
    with open("unfilteredoutput.txt", "w") as f:
        f.write(str(scrape_result))
    
    with open("unfilteredoutput.txt", "r") as file:
        text = file.read()
    
    # Clean up HTML tags and brackets
    result = re.sub(r"</?(strong|td)[^>]*>|[\[\]]", "", text)
    EnteredResult = result.replace(',', '\n')
    
    # Find controls
    controls = re.findall(r"\d+\.\d+\.\d+", result)
    
    # Save filtered output
    with open("FilteredOutput.txt", "w") as file:
        file.write(EnteredResult)
    
    # Extract text between controls
    extracted_texts = extract_text_between_numbers(result)
    return controls, extracted_texts

def make_system_content():
    with open("AISVS_C1.1.1(good).md", "r") as file:
        part1SystemContent = file.read()
    
    with open("SystemContentUnupdated.md", "r") as file:
        part2SystemContent = file.read()
    
    FullSystemContent = part2SystemContent
    print (FullSystemContent)
    return FullSystemContent

SystemContent = make_system_content()

# Loop through each URL
for url_index, url in enumerate(Url):
    controls, extracted_texts = process_url(url, url_index)
    print(f"Controls found: {controls}")

    # Loop through each control's text
# Inside the inner loop where you process each control
    for idx, control_text in enumerate(extracted_texts):
        control_number = controls[idx]  # e.g., '1.1.1'
        print(f"Processing control: {control_number}")
        
        with open("control_context.txt", "r") as file:
            control_context = file.read()


        control_textV2 = SystemContent + control_text + control_context + "this is the control your working on put that as the control id:" + control_number

        # Send to AI model
        response: ChatResponse = chat(
            model='gemma4',
            messages=[
                {'role': 'user', 'content': control_textV2}
            ],
            options={
                "num_ctx": 6000
            }
        )
    
        OllamaOutput = response.message.content
        print(OllamaOutput)
    
        # Save output to a file named with the control number
        filename = f"AISVS-C{control_number}.md"
        with open(filename, "w") as file:
            file.write(OllamaOutput)
