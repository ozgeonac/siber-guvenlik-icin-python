import subprocess
import datetime
import socket
import time
serverIP="127.0.0.1"
serverPort=514
while 1:
    time.sleep(60)
    macler=[]
    IPler=[]
    log=""
    sonuc=subprocess.check_output("arp -a",shell=True)
    #print sonuc
    try:
        for i in sonuc.split("\n"):
            macler.append(str(i).split(" ")[3])
            IPler.append(str(i).split(" ")[1][1:-1])
    except:
        pass
    print macler,"===\n"
    print IPler,"===\n"
    sayici=0
    an=str(datetime.datetime.now())
    log=log+str(an)
    for i in macler:
        #print macler.count(i)
        if int(macler.count(i)) > 1:
            print IPler[sayici]
            log=log+"|"+IPler[sayici]
            log=log+"|"+macler[sayici]
        sayici+=1
    print log
    print len(log)
    if len(log) >26:
        yazilacakLog=log+"\n"
        print "Gelen Log: ",yazilacakLog
        logDosya=open("log.txt","a")
        logDosya.write(yazilacakLog)
        logDosya.close()
        saldiriDosya=open("saldiri.txt","a")
        saldiriLog=str(an)+"|Arp poisoning\n"
        saldiriDosya.write(saldiriLog)
        saldiriDosya.close()
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.connect((serverIP,serverPort))
        server.send(yazilacakLog)
        server.send(saldiriLog)
        server.close()
