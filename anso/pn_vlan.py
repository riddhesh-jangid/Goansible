import random
import string
import os
from register import registerObj
import writer

class pn_vlan:
    playbook_name = ''
    hosts=[]
    register=[]
    pn_vlanid = ''
    state = ''
    pn_clipassword = ''
    pn_cliswitch = ''
    pn_cliusername = ''
    pn_description = ''
    pn_ports = ''
    pn_scope = ''
    pn_stats = ''
    pn_untagged_ports = ''
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

