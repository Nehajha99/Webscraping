# import requests
# from bs4 import BeautifulSoup
# import pprint
# import json
# url="https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471"
# r=requests.get(url)
# htmlcontent = r.content
# soup = BeautifulSoup(htmlcontent,"html.parser")
# div1 = soup.find_all("div",class_="_3WhJ")
# list1=[]
# s=1
# for i in div1:
#     name=i.find("div",class_="UGUy").get_text()
#     price=i.find("span").get_text()
#     link=i.find("a",class_="_8vVO")["href"]
#     details={"position":"","Name":"","Price":"","URL":""}
#     details["position"]=s
#     details["Name"]=name
#     details["Price"]=price
#     details["URL"]=link
#     s+=1
#     list1.append(details.copy())
#     with open("pickles_data.json","w") as file:
#         json.dump(list1,file,indent=4)
    

# from collections import UserString
# import requests
# from bs4 import BeautifulSoup
# import pprint
# import json
# url="https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471"
# r=requests.get(url)
# soup = BeautifulSoup(r.text,"html.parser")
# h=soup.find("div",class_="_1gX7")
# serial=h.span.get_text()
# p=serial.split()
# o=int(p[1])
# x=o//32+1
# list1=[]
# s=1
# j=1
# while j<=x:
#     Url="https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471&page="+str(j)
#     R=requests.get(Url)
#     Soup=BeautifulSoup(R.text,"html.parser")
#     div1 = Soup.find("div",class_="_3RA-")
#     Name=div1.find_all("div",class_="UGUy")
#     Price=div1.find_all("div",class_="_1kMS")
#     div2=div1.find_all("div",class_="_3WhJ")
#     i=0
#     while i<len(div1):
#         name=Name[i].get_text()
#         price=Price[i].get_text()
#         link=div2[i].a["href"]
#         likn1="https://paytmmall.com"+link
#         details={"position":"","Name":"","Price":"","URL":""}
#         details["position"]=s
#         details["Name"]=name
#         details["Price"]=price
#         details["URL"]=likn1
#         list1.append(details.copy())
#         s=s+1
#     j=j+1    
# with open("pickles_data.json","w") as file:
#     json.dump(list1,file,indent=4)
        