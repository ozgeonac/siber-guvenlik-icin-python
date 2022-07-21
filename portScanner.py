import telnetlib
host="192.168.213.168"
for port in range(1,1024,1):
    try:
        baglanti=telnetlib.Telnet(host,port)
        baglanti.write("\n")
        print "\n",str(port)," - ",baglanti.read_all().splitlines()[0]
        baglanti.close()
    except:
        pass
