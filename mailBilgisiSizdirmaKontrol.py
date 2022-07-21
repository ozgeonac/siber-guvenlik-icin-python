import re
import requests
url=""
istek=requests.get(url,verify=False)
sonuc=re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",istek.content)
print sonuc.group()
