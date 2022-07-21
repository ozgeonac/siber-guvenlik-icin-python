import itertools
import hashlib
sozlukListe=[[],[]]
karakterSeti='ab12'
karakter=raw_input("Max kac karakter olacak: ")
for i in range(1,int(karakter)+1,1):
    sonuc=itertools.combinations_with_replacement(karakterSeti,i)
    for password in sonuc:
            sozlukListe[0].append(''.join(password))
            sozlukListe[1].append(hashlib.md5(''.join(password)).hexdigest())
            #print  hashlib.md5(''.join(password)).hexdigest()
print "Sozluk:",sozlukListe[0]
print "Hashler:",sozlukListe[1]
