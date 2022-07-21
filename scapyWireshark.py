from scapy.all import *
packets = Ether()/IP(dst=Net("google.com"))/ICMP()
wireshark(packets)
