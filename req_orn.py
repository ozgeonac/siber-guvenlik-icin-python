import requests
domain=raw_input("Incelemek istediginiz domain: ")
sayfa=requests.get(domain)
print "Text: ",sayfa.text
print "Cookie: ",sayfa.cookies
print "Content: ",sayfa.content
print "Status code: ",sayfa.status_code
print "Headers: ",sayfa.headers
print "Links: ",sayfa.links
print "Request: ",sayfa.request
