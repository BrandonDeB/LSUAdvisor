import requests
from bs4 import BeautifulSoup
import xml.etree.cElementTree as ET
import majorSearch


class SemesterRecs():

    semester_num = ''
    classes = []


class DegreeProgram():

    major = ''
    concentration = ''
    semester = ''




def open_major(major: str):
    link = majorSearch.get_major_link(major)
    response = requests.get(link)
    major_html = response.text
    return major_html

# prints all the concentrations in the Major
def read_major(html, conc: str):
    parsed_html = BeautifulSoup(html, features="html.parser")
    concentrations = parsed_html.body.find_all('h3')
    full = " "
    for concentration in concentrations:
        if concentration.text == conc:
            full += "CONCENTRATION: " + concentration.text + "\n"
            for string in concentration.parent.nextSibling.strings:
                if len(string) > 1:
                    full += string + "\n"
    return full

# read_major(open_major('Agricultural & Extension Education, B.S'), "Agricultural Leadership and Development")

    

        
