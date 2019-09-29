import random
import string
import os
from register import registerObj
import writer

class ce_evpn_bgp_rr:
    playbook_name = ''
    hosts=[]
    register=[]
    as_number = ''
    bgp_evpn_enable = ''
    bgp_instance = ''
    peer = ''
    peer_type = ''
    policy_vpn_target = ''
    reflect_client = ''
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

