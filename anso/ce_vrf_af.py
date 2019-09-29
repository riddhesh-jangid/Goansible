import random
import string
import os
from register import registerObj
import writer

class ce_vrf_af:
    playbook_name = ''
    hosts=[]
    register=[]
    vrf = ''
    evpn = ''
    route_distinguisher = ''
    state = ''
    vpn_target_state = ''
    vpn_target_type = ''
    vpn_target_value = ''
    vrf_aftype = ''
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

