import random
import string
import os
from register import registerObj
import writer

class pn_igmp_snooping:
    playbook_name = ''
    hosts=[]
    register=[]
    state = ''
    pn_cliswitch = ''
    pn_enable = ''
    pn_enable_vlans = ''
    pn_igmpv2_vlans = ''
    pn_igmpv3_vlans = ''
    pn_no_snoop_linklocal_vlans = ''
    pn_query_interval = ''
    pn_query_max_response_time = ''
    pn_scope = ''
    pn_snoop_linklocal_vlans = ''
    pn_vxlan = ''
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

