import requests
from bs4 import BeautifulSoup
import xml.etree.cElementTree as ET
import re

url = "https://catalog.lsu.edu/content.php?catoid=27&navoid=2375";
response = requests.get(url)
major_listings = response.text

def get_all_major_elements():
    bs = BeautifulSoup(major_listings, features="html.parser")
    major_titles = bs.find_all('strong')
    temp = major_titles
    for x in reversed(range(len(major_titles))):
        if major_titles[x].text != 'Major':
            major_titles.remove(major_titles[x])

    major_titles = temp
    elements = []
    for listing in major_titles:
        listElements = listing.parent.find_next_sibling("ul").find("a")
        elements.append(listElements)

    return elements


def get_all_major_names():
    elements = get_all_major_elements()
    names = []
    for element in elements:
        names.append(element.text)
    return names

def get_all_major_links():
    elements = get_all_major_elements
    links = []
    for element in elements():
        links.append(element['href'])
    return links

def get_major_link(major: str):
    bs = BeautifulSoup(major_listings, features="html.parser")
    element = bs.find("a", string=re.compile(major))
    return 'https://catalog.lsu.edu/' + element['href']
        
print(get_major_link('Agricultural & Extension Education, B.S'))