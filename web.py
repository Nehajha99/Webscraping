# if you wants to scrape a website:
# 1. use api 
# 2. HTML web screaping using some tool like bs4

### step 0 : install all the requerments 
# pip install requests
# pip install bs4
# pip install html5lib
import pprint
import requests
from bs4 import BeautifulSoup
url="https://codewithharry.com"

### step 1 :get the HTML
r = requests.get(url)
htmlcontent = r.content
### step 2 : parse the HTML
soup = BeautifulSoup(htmlcontent,"html.parser")
#print(soup.prettify)

### step 3 : HTML tree traversal
#
## commonly used types of objects
# print(type(title))## 1. tag
# print(type(title.string))## 2. NavigableString
# print(type(soup))## 3. BeautifulSoup
## 4. comment
title=soup.title

# get all the paragraph from the page
#paras=soup.find_all("p")
#print(paras)

### get all the anchors tags  from the page
anchors=soup.find_all("a")
# print(anchors)
#####get all the links on the page:
# for link in anchors:
#     print(link.get("href"))

###get first element in the HTMLpage
#print(soup.find("p"))

###get all the classes of any elements in the HTML page
#print(soup.find("p")["class"])


#### find all the elements with class lead
#print(soup.find_all("p",class_="lead"))


###get the text from the tags?soup
#print(soup.find("p").get_text())

###
####get all the anchors tags  from the page
anchors=soup.find_all("a")
all_links=set()
####get all the links on the page:
for link in anchors:
    if (link.get("href")!="#"):
        linkText="https://codewithharry.com"+link.get("href")        
        all_links.add(link)
        print(linkText)


### 4 OBJECT COMMENT
# markup="<p><!--this is a comment --></p>"
# soup2=BeautifulSoup(markup)
# print(type(soup2.p.string))