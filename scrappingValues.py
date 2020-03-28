from bs4 import BeautifulSoup
import requests
url= "https://mohfw.gov.in/"
# getting the HTML
r = requests.get(url)
htmlContent=r.content

# Parsing the HTML

soup=BeautifulSoup(htmlContent,'html.parser')
#new code for state data
stateName='3'
State_name=int(stateName)-1
tempData = ""
# for t in soup.find_all('tbody')[9].find_all('tr'):
#     tempData += t.get_text()
# tempData = tempData[1:]
# StateList = []
# for i in tempData.split("\n\n"):
#     StateList.append(i.split("\n"))
# state_wise_cases=StateList[State_name]
# state_name=StateList[State_name]


#old code for state data
# stateName='1'
# State_name=int(stateName)-1
# statewises = soup.find_all("td")
# state_wise_cases=str(statewises[228])
# state_name=str(statewises[227])
# print(state_name, state_wise_cases,"\n",StateList)
def nationalCases():
    nationwide = soup.find_all("div")
    nation_wide_cases = int((nationwide[31].text)[1:6])
    return nation_wide_cases
def statewise(stateName):
    State_name=int(stateName)-1
    tempData = ""
    for t in soup.find_all('tbody')[9].find_all('tr'):
        tempData += t.get_text()
    tempData = tempData[1:]
    StateList = []
    for i in tempData.split("\n\n"):
        StateList.append(i.split("\n"))
    state_wise_cases=StateList[State_name][2]
    state_name=StateList[State_name][1]
    # statewises = soup.find_all("td")
    # state_wise_cases=str(statewises[228+6*State_name].text)
    # state_name=str(statewises[227+6*State_name].text)

    return state_wise_cases,state_name