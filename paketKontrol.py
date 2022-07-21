from scapy.all import *
payload=""
def payloadBul(paket):

    if paket.haslayer(Raw):
        payload = paket.getlayer(Raw).load
        if payload:
            print payload
            if 'Nessus' in payload:
                print "=====\n\n\nNessus taramasi var\n\n\n======="
    print "Ethernet src: ",str(paket['Ethernet'].src)
    print "Ethernet dst: ", str(paket['Ethernet'].dst)
    if paket['IP']:
        print "IP src: ", str(paket['IP'].src)
        print "IP dst: ", str(paket['IP'].dst)
    print "========================================\n\n"
                # # payload = paket.getlayer(Raw).load
                # # print "Payload: ",payload
sniff(iface="eth0",prn=payloadBul)
