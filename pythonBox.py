# import requests
# import pprint
# from bs4 import BeautifulSoup
# import json

# python_url="https://en.wikipedia.org/wiki/Python_(programming_language)"
# python_data=requests.get(python_url)
# htmlcontent=python_data.content
# soup=BeautifulSoup(htmlcontent,"html.parser")
# tr=soup.find_all("th",class_="infobox-label")
# td=soup.find_all("td",class_="infobox-data")
# dic={}
# for i in tr:
#     p=i.get_text()
#     print(p)
# for j in td:
#     pr=j.get_text()
#     print(pr)
#     #dic[p]=[pr]
# #print(dic)


import requests
import pprint
from bs4 import BeautifulSoup
import json

python_url="https://en.wikipedia.org/wiki/Python_(programming_language)"
python_data=requests.get(python_url)
htmlcontent=python_data.content
soup=BeautifulSoup(htmlcontent,"html.parser")
p=soup.find_all("p")
# # q=soup.find_all("a")
# # print(q)
for i in p[:20]:
    d=i.find("a")
    print(d)