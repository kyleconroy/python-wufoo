from wufoo.client import Wufoo
import logging

logging.basicConfig(level=logging.DEBUG)

ACCOUNT = "crofter"
TOKEN = "CEMR-2LYQ-73VD-F9JS"


wufoo = Wufoo(ACCOUNT, TOKEN)

for f in wufoo.forms.list():
    for field in f.fields.list():
        print field.title
        print field.type
