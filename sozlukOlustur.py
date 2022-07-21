import itertools
sozlukListe=[]
karakterSeti='ab12'
karakter=raw_input("Max kac karakter olacak: ")
for i in range(1,int(karakter)+1,1):
    sonuc=itertools.combinations_with_replacement(karakterSeti,i)
    for password in sonuc:
            sozlukListe.append(''.join(password))
print sozlukListe
