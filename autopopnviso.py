import re
import requests
from ollama import chat
from bs4 import BeautifulSoup
from ollama import ChatResponse

FirstControlPos = 1
SecondControlPos = 1
ThirdControlPos = 1

UrlVersion = 0

UrlFirstPart = "https://github.com/OWASP/AISVS/blob/main/1.0/en/0x10-"
Url = ["C01-Training-Data-Integrity-and-Traceability.md", "C02-Input-Validation.md", "C03-Model-Lifecycle-Management.md", "C04-Infrastructure.md", "C05-Access-Control-and-Identity.md", "C06-Supply-Chain.md", "C07-Model-Behavior.md", "C08-Memory-Embeddings-and-Vector-Database.md", "C09-Orchestration-and-Agentic-Action.md", "C10-MCP-Security.md", "C11-Adversarial-Robustness.md", "C12-Privacy.md", "C13-Monitoring-and-Logging.md", "C14-Human-Oversight.md",]


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
    done = soup.find_all("td", limit=2)
    print(done)
    with open("filteringtest.txt", "w") as f:
        f.write(str(done))
    
    with open("filteringtest.txt", "r") as file:
        text = file.read()

    result = re.sub(r"</?(strong|td)[^>]*>|[\[\]]", "", text)

    print(result)

    with open("filteringtest.txt", "w") as file:
        file = file.write(result)

    return result

FilterResponse()

AiInput = FilterResponse()

with open("AISystemContent.txt", "r") as file:
    AISystemContent = file.read()

response: ChatResponse = chat(model='gemma4', messages=[
    {
        'role': 'system',
        'content': 'please use a max of 2 lines',
    },
    {
    'role': 'user',
    'content': AISystemContent,
  },
])

OllamaOutput = response.message.content

print(OllamaOutput)

with open(f"AISVS-C{FirstControlPos}.{SecondControlPos}.{ThirdControlPos}.md", "w") as File:
    File.write(OllamaOutput)
