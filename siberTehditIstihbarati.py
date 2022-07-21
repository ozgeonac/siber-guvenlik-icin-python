# -*- coding: utf-8 -*-
import requests
import subprocess
import socket
import datetime
baglanti=raw_input("Bilgi sahibi olmak istediğiniz web sayfasını giriniz: ")
try:
    baglanti=socket.gethostbyaddr(baglanti)[2][0]
except:
    pass
response=requests.get('https://www.usom.gov.tr/url-list.txt',verify=False)
icerik=response.content
dosyaAdi=str(baglanti)+"-kontrol.txt"
komut="rm -rf "+str(dosyaAdi)
subprocess.call(komut,shell=True)
dosya = open(dosyaAdi, "a")
bugun=datetime.datetime.today()
yazi="Bu rapor "+str(baglanti)+" da yer alan IP adresi icin hazirlanmistir.\nTarih: "+str(bugun).split(" ")[0]+"\n=========\n"
dosya.write(yazi)
dosya.close()
for i in str(icerik).split("\n"):
    if baglanti in i:
        print "Girilen site zararlidir"
        dosya=open(dosyaAdi,"a")
        dosya.write("Usoum bilgilerine göre site zararlidir.\n")
        dosya.close()
url="https://virustotal.com/tr/domain/"+str(baglanti)+"/information/"

response=requests.get(url)
print "Virus total:",response.content
ServerNameBasla=str(response.content).find("Server Name")
ServerNameSon=str(response.content).find("</textarea>")
dosya=open(dosyaAdi,"a")
dosya.write(response.content[ServerNameBasla:ServerNameSon])
dosya.close()
print "Sonuc:",response.content[ServerNameBasla:ServerNameSon]
print "Sonuc:",response.content[ServerNameBasla:ServerNameSon]
sorgu="https://www.badips.com/get/info/"+str(baglanti)
response=requests.get(sorgu,verify=False)
#print response.json()['Listed']
try:
    if response.json()['Listed'] == False:
        badips=response.json()['suc']+"\n"
        dosya=open(dosyaAdi,"a")
        dosya.write(badips)
        dosya.close()
    else:
        icerik=response.json()
        print icerik
        ListStatusBadIPs="Bad IP Durumu: "+icerik['suc']+"\n"
        CountryBadIPs = "Ulke Bilgisi: "+icerik['CountryCode'] + "\n"
        #InetnumBadIPs = "IP araligi: "+icerik['Whois']['inetnum'] + "\n"
        #DescrBadIPs = "Bilgi:"+icerik['Whois']['descr'][0] + "\n" + icerik['Whois']['descr'][1] +"\n"
        ReportCountIPs = "Raporlanma Sayisi: "+str(icerik['ReporterCount']['sum']) +"\n"
        CategoryBadIPs = "Kategori: " +icerik['Categories'][0]+"\n"
        #badips=ListStatusBadIPs + CountryBadIPs + InetnumBadIPs + DescrBadIPs + ReportCountIPs + CategoryBadIPs
        badips = ListStatusBadIPs + CountryBadIPs  + ReportCountIPs + CategoryBadIPs
        dosya=open(dosyaAdi,"a")
        dosya.write(badips)
        dosya.close()
except:
    print "Bilgi elde edilemiyor..."
BlockListSSH=requests.get('https://lists.blocklist.de/lists/ssh.txt',verify=False)
print "BlockListSSH"
print BlockListSSH.content
print "============"
if baglanti in str(BlockListSSH.content):
    BlockListSSHBilgi=str(baglanti)+" son 48 icerisinde SSH servisi üzerinde bir saldiri icin blocklistde raporlanmistir.\n"
    dosya=open(dosyaAdi,"a")
    dosya.write(BlockListSSHBilgi)
    dosya.close()
else:
    BlockListSSHBilgi=str(baglanti)+" son 48 icerisinde SSH servisi üzerinde bir saldiri icin blocklistde raporlanmamistir.\n"
    dosya=open(dosyaAdi,"a")
    dosya.write(BlockListSSHBilgi)
    dosya.close()
BlockListMail=requests.get('https://lists.blocklist.de/lists/mail.txt',verify=False)
print "BlockListMail"
print BlockListMail.content
print "============"
if baglanti in str(BlockListMail.content):
    BlockListMailBilgi=str(baglanti)+" son 48 icerisinde mail servisi üzerinde bir saldiri icin blocklistde raporlanmistir.\n"
    dosya=open(dosyaAdi,"a")
    dosya.write(BlockListMailBilgi)
    dosya.close()
else:
    BlockListMailBilgi=str(baglanti)+" son 48 icerisinde mail servisi üzerinde bir saldiri icin blocklistde raporlanmamistir.\n"
    dosya=open(dosyaAdi,"a")
    dosya.write(BlockListMailBilgi)
    dosya.close()
BlockListApache=requests.get('https://lists.blocklist.de/lists/apache.txt',verify=False)
print "BlockListApache"
print BlockListApache.content
print "============"
if baglanti in str(BlockListApache.content):
    BlockListApacheBilgi=str(baglanti)+" son 48 icerisinde apache servisi üzerinden bir DDOS  veya RFI saldiri icin blocklistde raporlanmistir.\n"
    dosya=open(dosyaAdi,"a")
    dosya.write(BlockListApacheBilgi)
    dosya.close()
else:
    BlockListApacheBilgi=str(baglanti)+" son 48 icerisinde apache servisi üzerinden bir DDOS  veya RFI saldiri icin blocklistde raporlanmamistir.\n"
    dosya=open(dosyaAdi,"a")
    dosya.write(BlockListApacheBilgi)
    dosya.close()
BlockListImap=requests.get('https://lists.blocklist.de/lists/imap.txt',verify=False)
print "BlockListImap"
print BlockListImap.content
print "============"
if baglanti in str(BlockListImap.content):
    BlockListImapBilgi=str(baglanti)+" son 48 icerisinde Imap,Pop3 servisi üzerinden bir saldiri icin blocklistde raporlanmistir.\n"
    dosya=open(dosyaAdi,"a")
    dosya.write(BlockListImapBilgi)
    dosya.close()
else:
    BlockListImapBilgi=str(baglanti)+" son 48 icerisinde Imap,Pop3 servisi üzerinden bir saldiri icin blocklistde raporlanmamistir.\n"
    dosya=open(dosyaAdi,"a")
    dosya.write(BlockListImapBilgi)
    dosya.close()
BlockListFtp=requests.get('https://lists.blocklist.de/lists/ftp.txt',verify=False)
print "BlockListFtp"
print BlockListFtp.content
print "============"
if baglanti in str(BlockListFtp.content):
    BlockListFtpBilgi=str(baglanti)+" son 48 icerisinde FTP servisi üzerinden bir saldiri icin blocklistde raporlanmistir.\n"
    dosya=open(dosyaAdi,"a")
    dosya.write(BlockListFtpBilgi)
    dosya.close()
else:
    BlockListFtpBilgi=str(baglanti)+" son 48 icerisinde FTP servisi üzerinden bir saldiri icin blocklistde raporlanmamistir.\n"
    dosya=open(dosyaAdi,"a")
    dosya.write(BlockListFtpBilgi)
    dosya.close()
BlockListSip=requests.get('https://lists.blocklist.de/lists/sip.txt',verify=False)
print "BlockListSip"
print BlockListSip.content
print "============"
if baglanti in str(BlockListSip.content):
    BlockListSipBilgi=str(baglanti)+" SIP, VOIP serverlarına giris icin blocklistde raporlanmistir.\n"
    dosya=open(dosyaAdi,"a")
    dosya.write(BlockListSipBilgi)
    dosya.close()
else:
    BlockListSipBilgi=str(baglanti)+" SIP, VOIP serverlarına giris icin blocklistde raporlanmamistir.\n"
    dosya=open(dosyaAdi,"a")
    dosya.write(BlockListSipBilgi)
    dosya.close()
BlockListBots=requests.get('https://lists.blocklist.de/lists/bots.txt',verify=False)
print "BlockListBots"
print BlockListBots.content
print "============"
if baglanti in str(BlockListBots.content):
    BlockListBotsBilgi=str(baglanti)+" son 48 icerisinde RFI-Attacks, REG-Bots, IRC-Bots, BadBot saldirisi yaptigi icin blocklistde raporlanmistir.\n"
    dosya=open(dosyaAdi,"a")
    dosya.write(BlockListBotsBilgi)
    dosya.close()
else:
    BlockListBotsBilgi=str(baglanti)+" son 48 icerisinde RFI-Attacks, REG-Bots, IRC-Bots, BadBot saldirisi yaptigi icin blocklistde raporlanmamistir.\n"
    dosya=open(dosyaAdi,"a")
    dosya.write(BlockListBotsBilgi)
    dosya.close()
BlockListIRC=requests.get('https://lists.blocklist.de/lists/ircbot.txt',verify=False)
print "BlockListIRC"
print BlockListIRC.content
print "============"
if baglanti in str(BlockListIRC.content):
    BlockListIRCBilgi=str(baglanti)+" IRC Bot oldugu icin blocklistde raporlanmistir.\n"
    dosya=open(dosyaAdi,"a")
    dosya.write(BlockListIRCBilgi)
    dosya.close()
else:
    BlockListIRCBilgi=str(baglanti)+" IRC Bot oldugu icin blocklistde raporlanmamistir.\n"
    dosya=open(dosyaAdi,"a")
    dosya.write(BlockListIRCBilgi)
    dosya.close()
BlockListBruteForceLogin=requests.get('https://lists.blocklist.de/lists/bruteforcelogin.txt',verify=False)
print "BlockListBruteForceLogin"
print BlockListBruteForceLogin.content
print "============"
if baglanti in str(BlockListBruteForceLogin.content):
    BlockListBruteForceLoginBilgi=str(baglanti)+" Joomla,wordpress ve diğer web girisleri olabildigi icin blocklistde raporlanmistir.\n"
    dosya=open(dosyaAdi,"a")
    dosya.write(BlockListBruteForceLoginBilgi)
    dosya.close()
else:
    BlockListBruteForceLoginBilgi=str(baglanti)+" Joomla,wordpress ve diğer web girisleri olabildigi icin blocklistde raporlanmamistir.\n"
    dosya=open(dosyaAdi,"a")
    dosya.write(BlockListBruteForceLoginBilgi)
    dosya.close()
EmergingThreatBlockIP=requests.get('http://rules.emergingthreats.net/fwrules/emerging-Block-IPs.txt',verify=False)
print "EmergingThreatBlockIP"
print EmergingThreatBlockIP.content
print "============"
if baglanti in str(EmergingThreatBlockIP.content):
    EmergingThreatBlockIPBilgi=str(baglanti)+"  Emerging Threatte bloklanmistir.\n"
    dosya=open(dosyaAdi,"a")
    dosya.write(EmergingThreatBlockIPBilgi)
    dosya.close()
else:
    EmergingThreatBlockIPBilgi=str(baglanti)+"  Emerging Threatte bloklanmamistir.\n"
    dosya=open(dosyaAdi,"a")
    dosya.write(EmergingThreatBlockIPBilgi)
    dosya.close()
EmergingThreatComromisedIP=requests.get('http://rules.emergingthreats.net/blockrules/compromised-ips.txt',verify=False)
print "EmergingThreatComromisedIP"
print EmergingThreatComromisedIP.content
print "============"
if baglanti in str(EmergingThreatComromisedIP.content):
    EmergingThreatComromisedIPBilgi=str(baglanti)+"  Emerging Threatte Tehlikeli IP olarak belirlenmistir.\n"
    dosya=open(dosyaAdi,"a")
    dosya.write(EmergingThreatBlockIPBilgi)
    dosya.close()
else:
    EmergingThreatComromisedIPBilgi=str(baglanti)+"  Emerging Threatte Tehlikeli IP olarak belirlenmemistir.\n"
    dosya=open(dosyaAdi,"a")
    dosya.write(EmergingThreatBlockIPBilgi)
    dosya.close()
BinaryDefenceBanList=requests.get('http://www.binarydefense.com/banlist.txt',verify=False)
print "BinaryDefenceBanList"
print BinaryDefenceBanList.content
print "============"
if baglanti in str(BinaryDefenceBanList.content):
    BinaryDefenceBanListBilgi=str(baglanti)+"  Binary Defencede tehlikeli olarak belirlenmistir.\n"
    dosya=open(dosyaAdi,"a")
    dosya.write(BinaryDefenceBanListBilgi)
    dosya.close()
else:
    BinaryDefenceBanListBilgi=str(baglanti)+"  Binary Defencede tehlikeli olarak belirlenmemistir.\n"
    dosya=open(dosyaAdi,"a")
    dosya.write(BinaryDefenceBanListBilgi)
    dosya.close()
try:
    subprocess.call("curl https://reputation.alienvault.com/reputation.snort.gz",shell=True)
    sonuc=subprocess.check_call("ls   /Users/anilbaranyelken/Downloads/ | grep 'reputation.snort.gz'",shell=True)
    if int(sonuc)==0:
        subprocess.call("tar -zxvf /Users/anilbaranyelken/Downloads/reputation.snort.gz", shell=True)
        komut="cat /Users/anilbaranyelken/Downloads/reputation.snort | grep "+str(baglanti)
        sonuc=subprocess.check_output(komut,shell=True)
        print sonuc
        if sonuc:
            AlienVaultSonuc = "AlienVault Bilgi:\n" + str(sonuc) + "\n"
            dosya=open(dosyaAdi,"a")
            dosya.write(AlienVaultSonuc)
            dosya.close()
        else:
            AlienVaultSonuc = "AlienVault Bilgisi mevcut degildir\n"
            dosya=open(dosyaAdi,"a")
            dosya.write(AlienVaultSonuc)
            dosya.close()
except:
    print "Alienvault sekmesinde sorun olustu"
Openphish=requests.get('https://openphish.com/feed.txt',verify=False)
print "Openphish"
print Openphish.content
print "============"
if baglanti in str(Openphish.content):
    OpenphishBilgi=str(baglanti)+"  Openphishte phishing sosyal muhendislik saldirilarinda kullanilabilir olarak belirlenmistir.\n"
    dosya=open(dosyaAdi,"a")
    dosya.write(OpenphishBilgi)
    dosya.close()
else:
    OpenphishBilgi=str(baglanti)+"  Openphishte phishing sosyal muhendislik saldirilarinda kullanilabilir olarak belirlenmemistir.\n"
    dosya=open(dosyaAdi,"a")
    dosya.write(OpenphishBilgi)
    dosya.close()
ZeusBadIP=requests.get('https://zeustracker.abuse.ch/blocklist.php?download=badips',verify=False)
print "ZeusBadIP"
print ZeusBadIP.content
print "============"
if baglanti in str(ZeusBadIP.content):
    ZeusBadIPBilgi=str(baglanti)+"  Zeusta kotucul IP olarak belirlenmistir.\n"
    dosya=open(dosyaAdi,"a")
    dosya.write(ZeusBadIPBilgi)
    dosya.close()
else:
    ZeusBadIPBilgi=str(baglanti)+"  Zeusta kotucul IP olarak belirlenmemistir.\n"
    dosya=open(dosyaAdi,"a")
    dosya.write(ZeusBadIPBilgi)
    dosya.close()
ProjectHoneypotTurkiye=requests.get('https://www.projecthoneypot.org/list_of_ips.php?by=3&ctry=TR',verify=False)
if baglanti in ProjectHoneypotTurkiye.content:
    ProjectHoneypotTurkiyeBilgi=str(baglanti)+"  honeypot projesinde bad event olarak belirlenmistir.\n"
    dosya=open(dosyaAdi,"a")
    dosya.write(ProjectHoneypotTurkiyeBilgi)
    dosya.close()
else:
    ProjectHoneypotTurkiyeBilgi=str(baglanti)+"  honeypot projesinde bad event olarak belirlenmemistir.\n"
    dosya=open(dosyaAdi,"a")
    dosya.write(ProjectHoneypotTurkiyeBilgi)
    dosya.close()
print "======\n======\n======\n"+str(baglanti)+" icin uygulama sonlandi\n======\n======\n======\n"
