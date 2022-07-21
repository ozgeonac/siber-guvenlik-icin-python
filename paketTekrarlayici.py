from scapy.all import *
paketler=sniff(offline="deneme.pcap")
sayici=0
for i in paketler:
    sayici=sayici+1
    print str(sayici)," nolu paket:"
    print "Ethernet kaynak: ",str(i[Ether].src)
    print "Ethernet hedef: ",str(i[Ether].dst)
    print "IP kaynak: ",str(i[IP].src)
    print "IP kaynak: ",str(i[IP].dst)
    print "++++++++++++++++++++"
    yeniPaket=Ether(src=str(i[Ether].src),dst=str(i[Ether].dst))/IP(src=str(i[IP].src),dst=str(i[IP].dst))
    sendp(yeniPaket)
