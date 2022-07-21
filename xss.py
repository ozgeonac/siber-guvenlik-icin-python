# -*- coding: utf-8 -*-
import requests
yazi="http://192.168.43.44/xss/example1.php?name=hacker"
esittirIndis=yazi.find("=")
print esittirIndis
payload=["<h1>blackbox","111"]
for i in payload:
	istek=str(yazi[:esittirIndis+1])+str(i)
	print istek
	icerik=requests.get(istek)
	if i in icerik.content:
		print "XSS var..."
		print "Payload: ",str(i)
		print "================"
	else:
		print "XSS yok"
		print "==============="
