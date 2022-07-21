import _mysql
username=["root","toor"]
password=["root","toor"]
for i in username:
    for j in password:
        try:
            db=_mysql.connect(host="localhost",user=i,passwd=j,db="mysql")
            print(i, " username ve ", j, " parola icin giris yapildi")
        except:
            print(i," username ve ",j," parola icin giris yapilamadi")
