import random
import string
import os
from register import registerObj
import writer

class nxos_ospf_vrf:
    playbook_name = ''
    hosts=[]
    register=[]
    ospf = ''
    auto_cost = ''
    default_metric = ''
    log_adjacency = ''
    passive_interface = ''
    provider = ''
    router_id = ''
    state = ''
    timer_throttle_lsa_hold = ''
    timer_throttle_lsa_max = ''
    timer_throttle_lsa_start = ''
    timer_throttle_spf_hold = ''
    timer_throttle_spf_max = ''
    timer_throttle_spf_start = ''
    vrf = ''
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

