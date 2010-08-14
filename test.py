import keys
import logging
import unittest

from wufoo.resources import *
from wufoo.client import Wufoo

ACCOUNT = keys.PROD["account"]
KEY = keys.PROD["key"]

logging.basicConfig(level=logging.DEBUG)

class WufooTest(unittest.TestCase):

    def setUp(self):
        self.wufoo = Wufoo(ACCOUNT, KEY)

class UsersTest(WufooTest):
    
    def testGet(self):
        users = self.wufoo.users.list()

class ReportsTest(WufooTest):
    
    def testGet(self):
        reports = self.wufoo.reports.list()
        logging.debug(reports)

class FormsTest(WufooTest):
    
    def testList(self):
        forms = self.wufoo.forms.list()
        for form in forms:
            logging.debug(form.hash)

    def testGet(self):
        sid = "z7x4a9"
        form = self.wufoo.forms.get(sid)
        self.assertEquals(sid, form.hash)

if __name__ == '__main__':
    unittest.main()
