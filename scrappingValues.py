from bs4 import BeautifulSoup
import requests
url = "https://mohfw.gov.in/"
r = requests.get(url)
htmlContent = r.content
soup=BeautifulSoup(htmlContent, 'html.parser')


def nationalCases():
    active_cases = soup.find_all('li',{'class':'bg-blue'})[0].find_all('strong')[0].get_text()
    death_cases = soup.find_all('li', {'class': 'bg-red'})[0].find_all('strong')[0].get_text()
    recovered_cases = soup.find_all('li', {'class': 'bg-green'})[0].find_all('strong')[0].get_text()
    migrated_cases = soup.find_all('li', {'class': 'bg-orange'})[0].find_all('strong')[0].get_text()
    total_confirmed = str(int(active_cases) + int(death_cases) + int(recovered_cases) + int(migrated_cases))
    return active_cases,total_confirmed,death_cases,recovered_cases


def statewise(stateName):
    State_name=int(stateName)
    tempData = ""
    for t in soup.find_all('section', {'id': 'state-data', 'class': 'site-update'})[0].find_all('tr'):
        tempData += t.get_text()
    StateList = []
    for i in tempData.split("\n\n"):
        StateList.append(i.split("\n"))
    state_wise_cases = StateList[State_name][2]
    state_name = StateList[State_name][1]
    return state_wise_cases, state_name


