import random
import string
import os
from register import registerObj
import writer

class ios_l2_interface:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    access_vlan = ''
    aggregate = ''
    auth_pass = ''
    authorize = ''
    mode = ''
    native_vlan = ''
    provider = ''
    state = ''
    trunk_allowed_vlans = ''
    trunk_vlans = ''
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

