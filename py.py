import requests
from bs4 import BeautifulSoup as bss4
url = requests.get('https://wuzzuf.net/search/jobs/?q=Senior+Network+Security+Engineer&a=hpb')
soup = bss4(url.text,'html.parser')
job_name = soup.findAll('a',{'class':'css-o171kl'})
locations_names = soup.find_all("span", {"class": "css-5wys0k"})
job_skills = soup.find_all("div", {"class": "css-y4udm8"})
for i in range(len(locations_names)):
    print(job_name[i].text)
    print(locations_names[i].text)
    print(job_skills[i].text)






