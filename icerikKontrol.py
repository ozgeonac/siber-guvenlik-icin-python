# -*- coding: utf-8 -*-

import requests
import smtplib
import time
while 1:
    time.sleep(60)
    response=requests.get('https://a.wordpress.com')
    responseIcerik=response.content
    kontrol = 0
    dosya = open('icerik.txt','r')
    dosyaIcerik=dosya.readlines()
    dosya.close()
    for i in dosyaIcerik:
       if str(i).split("\n")[0] in responseIcerik:
          kontrol = kontrol + 1
    if len(dosyaIcerik) == kontrol:
        print "Web sayfasında değişiklik yok."
    else:
        print "Web sayfasında değişiklik yapılmıştır."
        try:
            gonderici = 'a@gmail.com'
            alici = 'a@gmail.com'
            mesaj = 'Web sayfasının içeriği değişti'
            username = 'a@gmail.com'
            password = '*****'
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.starttls()
            server.login(username, password)
            server.sendmail(gonderici, alici, mesaj)
            server.quit()
            print "Mail gönderildi"
        except:
            print "Mail gönderilemedi"
