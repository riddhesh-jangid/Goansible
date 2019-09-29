import random
import string
import os
from register import registerObj
import writer

class pn_vlag:
    playbook_name = ''
    hosts=[]
    register=[]
    pn_name = ''
    state = ''
    pn_clipassword = ''
    pn_cliswitch = ''
    pn_cliusername = ''
    pn_failover_action = ''
    pn_lacp_fallback = ''
    pn_lacp_fallback_timeout = ''
    pn_lacp_mode = ''
    pn_lacp_timeout = ''
    pn_mode = ''
    pn_peer_port = ''
    pn_peer_switch = ''
    pn_port = ''
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

