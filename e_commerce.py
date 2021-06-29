import pprint
import requests
from bs4 import BeautifulSoup
import json
url="https://webscraper.io/test-sites"
r=requests.get(url)
htmlcontent = r.content
soup = BeautifulSoup(htmlcontent,"html.parser")
div = soup.find_all("h2")
list1=[]
searial_number=1
for i in div:
   name=i.find("a").get_text().strip()
   link=i.find("a")["href"]
   details={"position":"","Name":"","URL":""}
   details["position"]=searial_number
   details["Name"]=name
   details["URL"]=link
   searial_number+=1
   list1.append(details.copy())
   with open("e_commerce.json","w") as file:
       json.dump(list1,file,indent=4)
   