from twisted.web import proxy, http
from twisted.internet import reactor
from twisted.python import log
import sys

class ProxyFactory(http.HTTPFactory):
    protocol = proxy.Proxy
class ClientFactory(proxy.ClientFactory):
    protocol = proxy.Proxy
log.startLogging(sys.stdout)
reactor.listenTCP(8080, ProxyFactory())
reactor.run()
