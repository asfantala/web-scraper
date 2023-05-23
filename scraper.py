import requests
from bs4 import BeautifulSoup
import json

def get_citations_needed_count(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    all_citations = soup.find_all('a', title="Wikipedia:Citation needed")
    return len(all_citations)

def get_citations_needed_report(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    all_p = soup.find_all('p')
    citations = []
    for citation in all_p:
        if citation.find('a', title="Wikipedia:Citation needed"):
            passage = citation.text.strip()
            citations.append(passage)
    return citations

def get_citations_needed_by_section():
    return

if __name__ == '__main__':
    url = 'https://en.wikipedia.org/wiki/History_of_Mexico'
    count = get_citations_needed_count(url)
    print(f"Number of citations needed: {count}")
    print(get_citations_needed_report(url))
    citations = get_citations_needed_report(url)
    report = {
        "count": count,
        "citations": citations
    }

    with open('citations_report.json', 'w') as file:
        json.dump(report, file, indent=4)
