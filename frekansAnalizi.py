# -*- coding: utf-8 -*-
metinIlk="blackbox"
metin=metinIlk.lower()
sozluk={"a":0,"b":0, "c":0, "ç":0, "d":0, "e":0, "f":0, "g":0, "ğ":0, "h":0, "i":0, "ı":0, "j":0, "k":0,"l":0, "m":0, "n":0, "o":0, "ö":0, "p":0, "r":0, "s":0, "ş":0, "t":0, "u":0, "ü":0, "v":0, "y":0, "z":0}
for i in metin:
    if i in sozluk: 
        sozluk[i]=sozluk[i]+1
for i in sozluk:
    print i,"-",sozluk[i]
