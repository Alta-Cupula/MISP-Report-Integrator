import requests
import re
from bs4 import BeautifulSoup


request = requests.get('https://www.crowdstrike.com/blog/observations-from-the-stellarparticle-campaign/')
#request = requests.get('https://resecurity.com/blog/article/blackcat-aka-alphv-ransomware-is-increasing-stakes-up-to-25m-in-demands')
soup = BeautifulSoup(request.content, 'html5lib')
text = soup.get_text()

def ip_finder(text):
    #patip = re.compile("")
    patip = re.compile("(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)")
    ips = patip.findall(text)
    
    return str(['.'.join(x) for x in ips])


#print(soup.prettify())
    

achou = ip_finder(text)

print(achou)