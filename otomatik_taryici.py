# -*- coding: utf-8 -*-
import os
IPRange=raw_input("IP Range: ")
print "netdiscover..."
os.system("echo '---Netdiscover---' >> otomatikTarayici.txt")
komut="netdiscover -r "+str(IPRange)+" >> otomatikTarayici.txt"
os.system(komut)
os.system("echo '---Dmitry---' >> otomatikTarayici.txt")
komut="dmitry -i "+str(IPRange)+" >> otomatikTarayici.txt"
os.system(komut)
print "nmap...."
os.system("echo '---Nmap---' >> otomatikTarayici.txt")
komut="nmap -sS -sV -vv "+str(IPRange)+" >> otomatikTarayici.txt"
os.system(komut)
print "hping3...."
os.system("echo '---hping3---' >> otomatikTarayici.txt")
komut="hping3 --scan 1-65000 -S -VV "+str(IPRange)+" >> otomatikTarayici.txt"
os.system(komut)
# komut="hping3 --tcp-timestamp -p 80 -S "+str(IPRange)+" >> otomatikTarayici.txt"
# os.system(komut)
print "nikto...."
os.system("echo '---Nikto---' >> otomatikTarayici.txt")
komut="nikto -h "+str(IPRange)+" >> otomatikTarayici.txt"
os.system(komut)
print "golismero...."
os.system("echo '---Golismero---' >> otomatikTarayici.txt")
komut="golismero scan "+str(IPRange)+" >> otomatikTarayici.txt"
os.system(komut)
print "wpscan...."
os.system("echo '---wpscan---' >> otomatikTarayici.txt")
komut="wpscan -u "+str(IPRange)+" >> otomatikTarayici.txt"
os.system(komut)
