import random
import string
import os
from register import registerObj
import writer

class pn_vrouter:
    playbook_name = ''
    hosts=[]
    register=[]
    pn_name = ''
    state = ''
    pn_bgp_as = ''
    pn_bgp_max_paths = ''
    pn_bgp_options = ''
    pn_bgp_redistribute = ''
    pn_clipassword = ''
    pn_cliswitch = ''
    pn_cliusername = ''
    pn_hw_vrrp_id = ''
    pn_ospf_options = ''
    pn_ospf_redistribute = ''
    pn_rip_redistribute = ''
    pn_router_id = ''
    pn_router_type = ''
    pn_service_state = ''
    pn_service_type = ''
    pn_vnet = ''
    pn_vrrp_track_port = ''
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

