import requests  
r = requests.get('https://www.marketsandmarkets.com/telecom-and-IT-market-research-113.html')

from bs4 import BeautifulSoup  
soup = BeautifulSoup(r.text, 'html.parser')  
appu = soup.find_all('tr', attrs={'class':'alt'})

records = [] 

for hab in appu:  
    title=hab.find({'h3': 'justify'}).text
    date=hab.find({'td': 'displaynone'}).find_next_sibling('td').text
    description=hab.find({'p': 'justify'}).text
    url=hab.find('a')['href']
    #print(title,date,description,url)

    records.append((title, date, description, url))  

import pandas as pd  
df = pd.DataFrame(records, columns=['Report_title',"Date_Published', Report_description','URL'])    
df.to_csv('99.csv', index=False, encoding='utf-8')
    
    

    