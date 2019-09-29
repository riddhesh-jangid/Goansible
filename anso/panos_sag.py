import random
import string
import os
from register import registerObj
import writer

class panos_sag:
    playbook_name = ''
    hosts=[]
    register=[]
    ip_address = ''
    operation = ''
    password = ''
    sag_name = ''
    api_key = ''
    commit = ''
    description = ''
    devicegroup = ''
    sag_match_filter = ''
    tags = ''
    username = ''
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

