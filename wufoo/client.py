import logging
from wufoo.core import Client
from wufoo.resources import *
from urllib import urlencode 
from urlparse import urljoin

class Wufoo(Client):
    """
    Http Client wrapper class, so we can 
    use whatever underlying http client
    """
    
    def __init__(self, account=None, token=None):
        base = "https://%s.wufoo.com" % account
        uri = "/api/v3"

        self.users   = Users(uri, client=self)
        self.reports = Reports(uri, client=self)
        self.forms   = Forms(uri, client=self)

        super(Wufoo, self).__init__(token, "footastic", base=base)
