import random
import string
import os
from register import registerObj
import writer

class ce_vxlan_tunnel:
    playbook_name = ''
    hosts=[]
    register=[]
    bridge_domain_id = ''
    nve_mode = ''
    nve_name = ''
    peer_list_ip = ''
    protocol_type = ''
    source_ip = ''
    state = ''
    vni_id = ''
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

