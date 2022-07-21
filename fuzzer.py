import requests
domain=raw_input("Domain: ")
dosya=open("fuzzListe.txt")
fuzzDosya=dosya.readlines()
for path in fuzzDosya:
    #print path
    url=domain+"/"+str(path)
    #print url
    baslangic=url.find("http")
    #print baslangic
    altsatirbaslangic=url.find("\n")
    #print altsatirbaslangic
    urlSon=url[baslangic:altsatirbaslangic]
    print urlSon
    sonuc=requests.get(urlSon)
    print "Durum: ",sonuc.status_code
    print "_____________________________"
