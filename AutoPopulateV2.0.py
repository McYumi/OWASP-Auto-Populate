import re
import requests
from ollama import chat
import subprocess, os, time
from ollama import ChatResponse

# List of URLs. Add the url for the control you wanna check for AISVS this is from C so for example C01-Training-Data-Integrity-and-Traceability.md
# for the ASVS this starts from the / after en so for example 0x10-V1-Encoding-and-Sanitization.md
Url = [
    "0x10-C01-Training-Data-Integrity-and-Traceability.md",
    "0x10-C02-Input-Validation.md",
]

#change this for AISVS = https://raw.githubusercontent.com/OWASP/AISVS/refs/heads/main/2.0-dev/en/0x10-
#change this for ASVS = https://raw.githubusercontent.com/OWASP/ASVS/refs/heads/master/5.0/en/
BaseUrl = "https://raw.githubusercontent.com/OWASP/AISVS/refs/heads/main/2.0-dev/en/"

def fetch_html(url):
    response = requests.get(url)
    print(response.status_code)
    response.raise_for_status()

    return response.text

def process_url():
    full_url = BaseUrl + url
    print(f"Processing URL: {full_url}")

    if os.path.exists(url) != True :
        subprocess.run(["wget", full_url])


    
#System content can and should be adjusted to get the perfect result for your needs.
def make_system_content():
    with open("SystemContent.md", "r") as file:
        part2SystemContent = file.read()
    
    FullSystemContent = part2SystemContent
    print (FullSystemContent)
    return FullSystemContent

SystemContent = make_system_content()

# Loop through each URL
for url_index, url in enumerate(Url):
    process_url()

    with open(url, "r") as file:
        control = file.read()

    controlNMBS = re.findall(r"\d+\.\d+\.\d+", control)
    print(f"Controls found: {controlNMBS}")

    AIPromt = SystemContent + control

    #print(AIPromt)

    for x in control:
    # Send to AI model
        try:
            response: ChatResponse = chat(
                model='gemma4',
                messages=[
                    {'role': 'user', 'content': AIPromt + f"make the skill sheet for each control individually please do this for control {controlNMBS}"}
                ],
                options={
                    "num_ctx": 8000
                }
            )
            print(control[x])
        except:
            print("error with the AI or the AI promt.")
        
            
    OllamaOutput = response.message.content
    print(OllamaOutput)

    # Save output to a file named with the control number
    filename = "AISVS-Ctest.md"
    with open(filename, "w") as file:
        file.write(OllamaOutput)
