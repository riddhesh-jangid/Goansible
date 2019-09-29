import random
import string
import os
from register import registerObj
import writer

class ce_vxlan_global:
    playbook_name = ''
    hosts=[]
    register=[]
    bridge_domain_id = ''
    nvo3_acl_extend = ''
    nvo3_ecmp_hash = ''
    nvo3_eth_trunk_hash = ''
    nvo3_gw_enhanced = ''
    nvo3_prevent_loops = ''
    nvo3_service_extend = ''
    state = ''
    tunnel_mode_vxlan = ''
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

