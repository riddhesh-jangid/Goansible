import random
import string
import os
from register import registerObj
import writer

class pn_stp_port:
    playbook_name = ''
    hosts=[]
    register=[]
    state = ''
    pn_block = ''
    pn_bpdu_guard = ''
    pn_cliswitch = ''
    pn_cost = ''
    pn_edge = ''
    pn_filter = ''
    pn_port = ''
    pn_priority = ''
    pn_root_guard = ''
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

