import random
import string
import os
from register import registerObj
import writer

class nxos_pim_interface:
    playbook_name = ''
    hosts=[]
    register=[]
    interface = ''
    border = ''
    dr_prio = ''
    hello_auth_key = ''
    hello_interval = ''
    jp_policy_in = ''
    jp_policy_out = ''
    jp_type_in = ''
    jp_type_out = ''
    neighbor_policy = ''
    neighbor_type = ''
    provider = ''
    sparse = ''
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

