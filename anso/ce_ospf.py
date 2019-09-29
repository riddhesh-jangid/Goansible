import random
import string
import os
from register import registerObj
import writer

class ce_ospf:
    playbook_name = ''
    hosts=[]
    register=[]
    process_id = ''
    addr = ''
    area = ''
    auth_key_id = ''
    auth_mode = ''
    auth_text_md5 = ''
    auth_text_simple = ''
    mask = ''
    max_load_balance = ''
    nexthop_addr = ''
    nexthop_weight = ''
    state = ''
    def compile(self):
       self.playbook_name=writer.writer(self,self.playbook_name)

    def run(self):
       dump_name=''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
       os.system('{} | tee {}'.format(self.playbook_name,dump_name))
       self.register = registerObj(dump_name)
       os.remove(dump_name)

    def go(self):
       self.compile()
       self.run()

