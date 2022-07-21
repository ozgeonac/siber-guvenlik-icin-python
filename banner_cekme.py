import telnetlib
host = raw_input("Host belirtiniz : ")
telnetBaglanti= telnetlib.Telnet(host,80)
telnetBaglanti.write("GET / HTTP/1.1\n")
komut="host: "+host+"\n\n\n\n"
telnetBaglanti.write(komut)
print telnetBaglanti.read_all()
