import random
import string
import os
from register import registerObj
import writer

class win_domain_group:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    attributes = ''
    category = ''
    description = ''
    display_name = ''
    domain_password = ''
    domain_server = ''
    domain_username = ''
    ignore_protection = ''
    managed_by = ''
    organizational_unit = ''
    protect = ''
    scope = ''
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

