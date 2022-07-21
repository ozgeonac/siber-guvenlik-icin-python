import requests
sonuc=requests.get("http://ipinfo.io/json",verify=False)
SonucJson=sonuc.json()
print SonucJson['loc']
