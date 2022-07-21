from suds.client import Client
import json
url="http://www.webservicex.com/globalweather.asmx?WSDL"
client=Client(url)
print "Client bilgileri : ",client,"\n"
print "Ulkemizdeki hava durumu bilgisi alinan iller: ",client.service.GetCitiesByCountry("Turkey"),"\n"
print "Ankara/Esenboga Hava Durumu: ",client.service.GetWeather("Ankara / Esenboga","Turkey"),"\n"
