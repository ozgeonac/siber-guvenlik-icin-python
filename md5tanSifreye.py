import itertools
import hashlib
karakterSeti='abcdefghijklmnoprstuvyz'
karakter=raw_input("Max kac karakter olacak: ")
md5=raw_input("Md5 giriniz: ")
for i in range(1,int(karakter)+1,1):
    sonuc=itertools.combinations_with_replacement(karakterSeti,i)
    for password in sonuc:
        if md5==hashlib.md5(''.join(password)).hexdigest():
            print "Sifre: ",str(''.join(password))
