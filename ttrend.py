import requests
from bs4 import BeautifulSoup

list= []
url = "http://trends24.in/india/~cloud"
sc = requests.get(url)
soup = BeautifulSoup(sc.text,"lxml")
li = soup.find_all('li')
for data in li:
    list.append((data.find('a').text))
for i in list:
    if(i[1]=='#'):
        print(i)
        print('-----------')
    
#print(soup.prettify())


'''</h1>data.find('description').text)
   <div class="page-content__tagcloud">
    <ol class="page-content__tagcloud__list" id="cloud-ol">
     <li>
      <a data-count="14" href="http://twitter.com/search?q=%23HappyBirthdayJacqueline" style="opacity:2.81;font-size:281%;">
       #HappyBirthdayJacqueline
      </a>
     </li>
     <li>
      <a data-count="14" href="http://twitter.com/search?q=%23IamWinvestor" style="opacity:2.81;font-size:281%;">
       #IamWinvestor
      </a>
     </li>
     <li>
      <a data-count="13" href="http://twitter.com/search?q=%23RSSMuktBharat" style="opacity:2.64;font-size:264%;">
       #RSSMuktBharat
      </a>
     </li>
     <li>'''