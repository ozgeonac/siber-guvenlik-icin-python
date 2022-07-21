from vulndb import DBVuln
print DBVuln.get_all_db_ids()
for i in DBVuln.get_all_db_ids():
    print i," nolu zafiyet basligi :",DBVuln.from_id(i).title
    print "Zafiyet tanimi: ",DBVuln.from_id(i).description
    print "Zafiyet detayi: ",DBVuln.from_id(i).fix_guidance
    print "Risk: ",DBVuln.from_id(i).severity
    if DBVuln.from_id(i).cwe:
        for j in DBVuln.from_id(i).cwe:
            print "CVE Url: ",DBVuln.from_id(i).get_cwe_url(j)
    print "---------------------------------------------------------"
