# -*- coding: utf-8 -*-
import os
import hashlib
import xlrd
os.system("find /home/toor/Downloads  >> dizin.txt")
dosya=open("dizin.txt")
dizin=dosya.readlines()
excel = xlrd.open_workbook("hash.xls")
ilkSayfa = excel.sheet_by_index(0)
print ilkSayfa.nrows
for path in dizin:
    path=path[:-1]
    try:
        hash=str(hashlib.md5(open(path, 'rb').read()).hexdigest())
        for i in range(2,ilkSayfa.nrows,1):
            if ilkSayfa.row_values(i)[0] == hash:
                print "Dosya zararlı, zararlı adı : ",ilkSayfa.row_values(i)[1]
                print "Path: ", path
                print "Md5 hash: ", hash
                print "--------------"
    except IOError,KeyboardInterrupt:
        continue

print "Tarama işlemi tamamlandı"
