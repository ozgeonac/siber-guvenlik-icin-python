# -*- coding: cp1254 -*-
def ceasarSifreleme(yazi,otelemeMiktari):
    sifreyazi = ""
    yaziListe = []
    yaziSayi = []
    yaziListe = list(yazi)
    #print yaziListe
    for i in yaziListe:
        yaziSayi = ord(i) + otelemeMiktari
        sifreyazi = sifreyazi + chr(yaziSayi)
    return sifreyazi
def ceasarSifreCoz(yazi):
    duzyazi = ""
    yaziListe = []
    yaziSayi = []
    yaziListe = list(yazi)
    #print yaziListe
    for otelemeMiktari in range(1,29):
        for i in yaziListe:
            yaziSayi = ord(i) - otelemeMiktari
            duzyazi = duzyazi + chr(yaziSayi)
        print str(otelemeMiktari)+" harf kadar ötelenmiş düz metin : "+ duzyazi
        duzyazi=""
print "----Sezar Şifreleme----"
ceasarSifre=ceasarSifreleme("merhaba",3)
print "Şifreli metin : "+ceasarSifre
print "----Sezar Şifre Çözme----"
ceasarSifreCoz(ceasarSifre)
