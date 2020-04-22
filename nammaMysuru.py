from bs4 import BeautifulSoup
import requests
url = "https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Karnataka"
r = requests.get(url)
htmlContent = r.content
soup = BeautifulSoup(htmlContent, 'html.parser')
mysuru = soup.find_all('tbody')[6].find_all('tr')[16].find_all('td')


def nammaMysuru():
    confirmed_cases = mysuru [0].get_text()
    recovered_cases = mysuru [1].get_text()
    active_cases = mysuru [2].get_text()
    death_cases = mysuru [3].get_text()
    return active_cases,confirmed_cases,death_cases,recovered_cases