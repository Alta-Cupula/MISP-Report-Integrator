import re

import requests
from bs4 import BeautifulSoup

request = requests.get('https://www.crowdstrike.com/blog/observations-from-the-stellarparticle-campaign/')
soup = BeautifulSoup(request.content, 'html5lib')
text = soup.get_text()

def ip_finder(text):
    patip = re.compile("(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)")
    ips = patip.findall(text)
    
    return str(['.'.join(x) for x in ips])


    

achou = ip_finder(text)

print(achou)
