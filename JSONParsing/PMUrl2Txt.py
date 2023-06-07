import json
import urllib.request
import sys
from urllib.error import HTTPError

content = []
i = 0

# Read the list of 8-digit numbers from the file
with open('pubmed.txt', 'r') as f:
    numbers = [line.strip() for line in f]

# Create the list of URLs
base_url = 'https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_json/{}/unicode'
urls = [base_url.format(number) for number in numbers]

# Iterate over the list of URLs and run the given routine for each one
for url in urls:
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            for document in data['documents']:
                for passage in document['passages']:
                    content.append(passage['text'])
                    content.append("\n")
    except HTTPError as e:
        print("An HTTP error occurred! This usually means that the PMID was not found in PMIC.")
        print(e)
        sys.exit()
    fileWriter = open("output\\"+numbers[i]+".txt", 'w', encoding="utf-8")
    fileWriter.writelines(content)
    fileWriter.close()
    content.clear()
    i += 1
