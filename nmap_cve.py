import nmap
import requests
import webbrowser
#python-nmap
nmap = nmap.PortScanner()
nmap.scan('127.0.0.1', '1-55','-sV')
print "Nmap komutu: ",nmap.command_line()
print "Tarama bilgisi: ",nmap.scaninfo()
print "Tarama durumu: ",nmap.scanstats()
print "Hostlar: ",nmap.all_hosts()
deger=0
try:
    for i in nmap.csv().split("\n"):
        # #print i
        # print "Product: ",i.split(';')[5]
        # print "Versiyon: ",i.split(';')[8]
        if not deger==0:
            Servis=str(i.split(';')[5])+" "+str(i.split(';')[8])
            print Servis
            print "__________________________________"
            print "CVE Details Bilgileri"
            print "__________________________________"
            url='http://www.cvedetails.com/google-search-results.php?q='+str(i.split(';')[5])+'&sa=Search'
            sayfa = requests.get(url)
            content = str(sayfa.content)
            print content
            webbrowser.open_new(url)
        deger=deger+1

except IndexError:
    print "Son satira gecildi"
