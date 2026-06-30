AutoPop is a project to automatically populate a skill sheet for OWASP ASVS and AISVS

It uses AI to quickly populate the skill sheet, and scrapes the control info for a more accurate result.
It also uses a specific System content to make it more accurate and consise. 
Mostly a high level view of the control but goes into detail for some headers of the skill sheet. 
It is made to make the controls easier to work with, since some controls can be unclear this will tell you how to test for a control and whats needed.
It will also try to tell you if it can be completely automated by an AI or if its need human interaction.

ALWAYS check the output since it is AI generated mistakes can be made, and hallucination does happen sometimes.

If needed it could also just be used as a scrape tool to quickly get controls and subcontrols for AISVS and ASVS.

There's currently 2 versions of this script:

V1.1 uses beautifulsoup to scrape github.com it also has some more safety features to have better error handeling.

V2.0 uses wget to download raw.githubusercontent.com and then uses that. Which saves loads of processing because it doesnt need to clean the output.
V2.0 is not currently working properly.
