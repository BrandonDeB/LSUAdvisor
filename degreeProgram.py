import requests
from bs4 import BeautifulSoup
import xml.etree.cElementTree as ET


class SemesterRecs():

    semester_num = ''
    classes = []


class DegreeProgram():

    major = ''
    concentration = ''
    semester = ''




def open_major(major: str):
    tree = ET.parse("majors.xml")
    root = tree.getroot()
    link = ''
    for degree in root:
        name = degree.find('Name').text.strip()
        if name == major:
            print('found')
            link = degree.find('Link').text
            break
    link = link.replace('&amp;', '&').strip()
    response = requests.get(link)
    major_html = response.text
    return major_html

def read_major(html):
    parsed_html = BeautifulSoup(html, features="html.parser")
    concentrations = parsed_html.body.find_all('h3')
    for concentration in concentrations:
        print(concentration.text)



read_major(open_major('Agricultural & Extension Education, B.S'))

    

        
