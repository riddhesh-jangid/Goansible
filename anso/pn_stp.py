import random
import string
import os
from register import registerObj
import writer

class pn_stp:
    playbook_name = ''
    hosts=[]
    register=[]
    state = ''
    pn_bpdus_bridge_ports = ''
    pn_bridge_id = ''
    pn_bridge_priority = ''
    pn_cliswitch = ''
    pn_enable = ''
    pn_forwarding_delay = ''
    pn_hello_time = ''
    pn_max_age = ''
    pn_mst_config_name = ''
    pn_mst_max_hops = ''
    pn_root_guard_wait_time = ''
    pn_stp_mode = ''
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

