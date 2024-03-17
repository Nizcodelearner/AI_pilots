import requests
from bs4 import BeautifulSoup

# crawling logic... 

def getSbti(company):
    sbti_url="https://sciencebasedtargets.org/resources/runtime/1710419465.json"
    resp=requests.get(sbti_url)
    if resp.status_code != 200:
        return False
    data=resp.json()
    compdata=data['data']
    for c_data in compdata:
        if c_data['company']==company:
            return True
    
    return False

def getCdpScore(company):
    cdp_url="https://www.cdp.net/en/responses?per_page=20&queries%5Bname%5D=#COMP#&sort_by=project_year&sort_dir=desc"

    cdp_url=cdp_url.replace("#COMP#",company)
    response = requests.get(cdp_url)
    soup = BeautifulSoup(response.content, "html.parser")
    tables=soup.select("table")
    table=tables[0]
    header = []
    rows = []
    scoreinfo=[]
    for i, row in enumerate(table.find_all('tr')):
        if i == 0:
            header = [el.text.strip() for el in row.find_all('th')]
        else:
            rows.append([el.text.strip() for el in row.find_all('td')])
    for row in rows:
        scoreinfo.append("For the Comapnay "+row[0]+" "+row[1]+ " Score is:"+row[4].replace("\n",""))

    for score in scoreinfo:
        print(score)

print("starting Program")
Scorelist=getCdpScore("sfp")
status=getSbti("Tata Motors Limited")
print("Stbi Status:",status)
#Deutsche Glasfaser Group GmbH
