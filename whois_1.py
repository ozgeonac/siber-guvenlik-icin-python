import whois
#python-whois yuklenecek
#futures yuklenecek
domain=raw_input("Domain: ")
sorgu = whois.whois(domain)
print "Domain: ",sorgu.domain
print "Anahtar kelimeler: ",sorgu.items()
print "Update time: ",sorgu.get('updated_date')
print "Expiration time: ",sorgu.get('expiration_date')
print "Name server: ",sorgu.get('name_servers')
print "Email: ",sorgu.get('emails')
