import pcapy
import struct
import socket
cihazlar=pcapy.findalldevs()
print cihazlar
paketler=pcapy.open_live('eth0',65536,1,0)#eth0 bir paketteki 65536 byte prom.mode timeout 0
while 1:
    (header,payload)=paketler.next()
    ethernet=struct.unpack('!6s6sH',payload[0:14])
    #big endian 6 short 6 short unsogned integer 6+6+2=14
    #print ethernet
    print "Ethernet protokolu",socket.ntohs(ethernet[2])
    print '%.2x-%.2x-%.2x-%.2x-%.2x-%.2x' %(ord(ethernet[0][0]),ord(ethernet[0][1]),ord(ethernet[0][2]),ord(ethernet[0][3]),ord(ethernet[0][4]),ord(ethernet[0][5]))
