import random
import string
import os
from register import registerObj
import writer

class cv_server_provision:
    playbook_name = ''
    hosts=[]
    register=[]
    host = ''
    password = ''
    server_name = ''
    switch_name = ''
    switch_port = ''
    template = ''
    username = ''
    action = ''
    auto_run = ''
    port = ''
    port_vlan = ''
    protocol = ''
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

