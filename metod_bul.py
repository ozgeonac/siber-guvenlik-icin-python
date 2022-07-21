import telnetlib
host = raw_input("Domain : ")
telnetBaglanti= telnetlib.Telnet(host,80)
telnetBaglanti.write("OPTIONS / HTTP/1.1\n")
komut="Host: "+host+"\n\n\n\n"
telnetBaglanti.write(komut)
sayfa=telnetBaglanti.read_all()
deger=str(sayfa).find("Allow")
Metodlar=sayfa[deger:deger+40]
print "Metodlar: ",Metodlar
if str(sayfa).find("PUT"):
    print "File upload yapilabilir..."
