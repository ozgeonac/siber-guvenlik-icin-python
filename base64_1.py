# -*- coding: utf-8 -*-
import base64
yazi="deneme"
base64encode=base64.b64encode(yazi)
print "Base64 encode edilmiş: ",base64encode
base64decode=base64.b64decode(base64encode)
print "Base64 decode edilmiş: ",base64decode
