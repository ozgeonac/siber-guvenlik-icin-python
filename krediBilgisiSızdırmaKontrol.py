import re
import requests
url=""
istek=requests.get(url,verify=False)
icerik=str(istek).split()
icerikSon=str("".join(icerik))
AMEX = re.match(r"^3[47][0-9]{13}$",icerikSon)
VISA = re.match(r"^4[0-9]{12}(?:[0-9]{3})?$",icerikSon)
MASTERCARD = re.match(r"^5[1-5][0-9]{14}$",icerikSon)
DISCOVER = re.match(r"^6(?:011|5[0-9]{2})[0-9]{12}$",icerikSon)
try:
    if MASTERCARD.group():
        print "Master Card bulundu!"
        print MASTERCARD.group()
except:
    print "Mastercard bulunamadi!"

try:
    if VISA.group():
        print "Visa bulundu!"
        print VISA.group()
except:
    print "Visa bulunamadi!"

try:
    if AMEX.group():
        print "AMEX Card bulundu!"
        print AMEX.group()
except:
    print "AMEX bulunamadi!"

try:
    if DISCOVER.group():
        print "DISCOVER Card bulundu!"
        print DISCOVER.group()
except:
    print "DISCOVER bulunamadi!"
