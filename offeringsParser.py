from bs4 import BeautifulSoup
import requests
from dict2xml import dict2xml
import re

base_url = 'https://appl101.lsu.edu/booklet2.nsf/f5e6e50d1d1d05c4862584410071cd2e?CreateDocument'
params = {"%%Surrogate_SemesterDesc":"1",
"SemesterDesc":"Spring 2024",
"%%Surrogate_Department":"1",
"Department":"COMPUTER SCIENCE"}
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
"Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
"Accept-Language" : "en-US,en;q=0.5",
"Accept-Encoding" : "gzip, deflate, br",
"Origin" : "https://appl101.lsu.edu",
"Referer" : "https://appl101.lsu.edu/booklet2.nsf/Selector2?OpenForm",
"Upgrade-Insecure-Requests" : "1",
"Sec-Fetch-Dest" : "frame",
"Sec-Fetch-Mode" : "navigate",
"Sec-Fetch-Site" : "same-origin",
"Sec-Fetch-User" : "?1" }
pem = 'appl101-lsu-edu-chain.pem'

course_id_dict = {}

def get_department_names():
    selector_url = 'https://appl101.lsu.edu/booklet2.nsf/Selector2?OpenForm'
    response = requests.post(selector_url, verify='appl101-lsu-edu-chain.pem')
    names = []
    soup = BeautifulSoup(response.content, 'html.parser')
    results = soup.findAll("select", {"name" : "Department"})
    for result in results:
        listing = result.text.strip().split('\n')
        for name in listing:
            names.append(name)

    return names

def retreive_html(semester, department):
    params.update({'SemesterDesc':semester, 'Department':department})

    response = requests.post(base_url, params, headers=headers, verify='appl101-lsu-edu-chain.pem')
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup.text

def get_department_ids(names):
    for name in names[:10]:
        html = retreive_html('Spring 2024', name)
        html = html.strip()
        broken_up = html.splitlines()
        if html.find('There are no courses found for this Semester') == -1:
            line = broken_up[5]
            abbr = line[11:15]
            abbr = abbr.strip()
            course_id_dict[re.sub('[^a-zA-Z_ ]', '', name)]=abbr

names = get_department_names()
get_department_ids(names)

xml = dict2xml(course_id_dict)

f = open("dictionary.xml", "w")
f.write(xml)
f.close()

