import re
import requests
from ollama import chat
from bs4 import BeautifulSoup
from ollama import ChatResponse

i = 0

FirstControlPos = 1
SecondControlPos = 1
ThirdControlPos = 1

UrlVersion = 0

UrlFirstPart = "https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-"

Url = ["C01-Training-Data-Integrity-and-Traceability.md", "C02-Input-Validation.md", "C03-Model-Lifecycle-Management.md", "C04-Infrastructure.md", "C05-Access-Control-and-Identity.md", "C06-Supply-Chain.md", "C07-Model-Behavior.md", "C08-Memory-Embeddings-and-Vector-Database.md", "C09-Orchestration-and-Agentic-Action.md", "C10-MCP-Security.md", "C11-Adversarial-Robustness.md", "C12-Privacy.md", "C13-Monitoring-and-Logging.md", "C14-Human-Oversight.md",]
FinalUrlIndex = len(Url)

def extract_text_between_numbers(text):
    # Pattern to match the numbered patterns (e.g., 1.1.1, 1.10.10)
    pattern = r'\d+(?:\.\d+)+'
    
    # Find all matches of the numbered patterns
    matches = list(re.finditer(pattern, text))
    
    # Extract the text between the matches
    results = []
    for i in range(len(matches) - 1):
        start = matches[i].end()
        end = matches[i + 1].start()
        # Get the text between the current match and the next
        between_text = text[start:end].strip()
        if between_text:
            results.append(between_text)
    return results

def UrlControl():
    FullUrl = ("https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-"+Url[UrlVersion])
    print(FullUrl)
    return FullUrl

FullUrl = UrlControl()

def ServerRequest():
    response = requests.get(FullUrl)
    HtmlData = response.text
    return HtmlData

html_doc = ServerRequest()

soup = BeautifulSoup(html_doc, 'html.parser')

FullResponse = ServerRequest()

def FilterResponse():
    ScrapeResult = soup.find_all("td", limit=75)
    print(ScrapeResult)
    with open("unfilteredoutput.txt", "w") as f:
        f.write(str(ScrapeResult))
    
    with open("unfilteredoutput.txt", "r") as file:
        text = file.read()

    result = re.sub(r"</?(strong|td)[^>]*>|[\[\]]", "", text)

    #print(result)

    EnteredResult = result.replace(',', '\n')

    controls = re.findall(r"\d+\.\d+\.\d+", result)

    with open("FilteredOutput.txt", "w") as file:
        file = file.write(EnteredResult)

    return controls, result

controls, result = FilterResponse()

#AiInput = result

#print(controls)

extracted_texts = extract_text_between_numbers(result)
print(extracted_texts[0])

with open("SystemContent.txt", "r") as file:
    AISystemContent = file.read()

#print(AISystemContent)

with open("ScrapeAISVSC1.1.1.txt", "r") as file:
    AIUserContent = file.read()
print(controls)

response: ChatResponse = chat(model='gemma4', messages=[
    {
        'role': 'system',
        'content': AISystemContent,
    },
    {
    'role': 'user', 
    'content': extracted_texts[0],
    },
])

OllamaOutput = response.message.content

print(OllamaOutput)

with open(f"AISVS-C{FirstControlPos}.{SecondControlPos}.{ThirdControlPos}.md", "w") as File:
    File.write(OllamaOutput)
