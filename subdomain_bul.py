import requests
import re
#https://cyberstruggle.org
domain=raw_input("Incelemek istediginiz domain: ")
sayfa=requests.get(domain)
content=str(sayfa.content)
#print "content: ",content
subdomain=""
for a in list(re.finditer('href=', content)):
    son=a.end()
    deger=son
    while not content[deger]=='"':
        deger=deger+1
        subdomain=content[son:deger]

    print subdomain
