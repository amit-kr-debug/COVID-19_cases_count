from bs4 import BeautifulSoup
import requests
url= "https://mohfw.gov.in/"
# getting the HTML
r = requests.get(url)
htmlContent=r.content

# Parsing the HTML

soup=BeautifulSoup(htmlContent,'html.parser')
#new code for state data
# stateName='28'
# State_name=int(stateName)
# tempData = ""
# for t in soup.find_all('section',{'id':'state-data','class':'site-update'})[0].find_all('tr'):
#     tempData += t.get_text()
# StateList = []
# for i in tempData.split("\n\n"):
#     StateList.append(i.split("\n"))
# # total_confirmed=StateList[30][1]
# death_cases=soup.find_all('li',{'class':'bg-red'})[0].find_all('strong')[0].get_text()
# recovered_cases=soup.find_all('li',{'class':'bg-green'})[0].find_all('strong')[0].get_text()
#

#
#old code for state data
# stateName='1'
# State_name=int(stateName)-1
# statewises = soup.find_all("td")
# state_wise_cases=str(statewises[228])
# state_name=str(statewises[227])
# print(state_name, state_wise_cases,"\n",StateList)
# print(tempData)
# print(total_confirmed,death_cases,recovered_cases,StateList)
def nationalCases():
    active_cases = soup.find_all('li',{'class':'bg-blue'})[0].find_all('strong')[0].get_text()
    death_cases = soup.find_all('li', {'class': 'bg-red'})[0].find_all('strong')[0].get_text()
    recovered_cases = soup.find_all('li', {'class': 'bg-green'})[0].find_all('strong')[0].get_text()
    migrated_cases = soup.find_all('li', {'class': 'bg-orange'})[0].find_all('strong')[0].get_text()
    total_confirmed = str(int(active_cases)+ int(death_cases)+ int(recovered_cases)+int(migrated_cases))
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
    # second code
    # for t in soup.find_all('tbody')[9].find_all('tr'):
    #     tempData += t.get_text()
    # tempData = tempData[1:]
    # StateList = []
    # for i in tempData.split("\n\n"):
    #     StateList.append(i.split("\n"))
    # state_wise_cases=StateList[State_name][2]
    # state_name=StateList[State_name][1]

    # first code
    # statewises = soup.find_all("td")
    # state_wise_cases=str(statewises[228+6*State_name].text)
    # state_name=str(statewises[227+6*State_name].text)

    return state_wise_cases,state_name


# a,b,c,d=nationalCases()
# print(a,b,c,d)