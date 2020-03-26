from bs4 import BeautifulSoup
import requests
url= "https://mohfw.gov.in/"
# getting the HTML
r = requests.get(url)
htmlContent=r.content

# Parsing the HTML

soup=BeautifulSoup(htmlContent,'html.parser')
statewises=soup.find_all("td")
# stateName='a'
# State_name=ord(stateName)-96
# statewises = soup.find_all("td")
# state_wise_cases=str(statewises[220].text)
# state_name=str(statewises[219].text)
# print(state_name, state_wise_cases)
def nationalCases():
    nationwide = soup.find_all("div")
    nation_wide_cases = int((nationwide[31].text)[1:6])
    return nation_wide_cases
def statewise(stateName):
    State_name=ord(stateName)-96
    statewises = soup.find_all("td")
    state_wise_cases=str(statewises[220+6*State_name].text)
    state_name=str(statewises[219+6*State_name].text)

    return state_wise_cases,state_name



