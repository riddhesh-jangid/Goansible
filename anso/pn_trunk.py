import random
import string
import os
from register import registerObj
import writer

class pn_trunk:
    playbook_name = ''
    hosts=[]
    register=[]
    pn_name = ''
    state = ''
    pn_broadcast_level = ''
    pn_clipassword = ''
    pn_cliswitch = ''
    pn_cliusername = ''
    pn_description = ''
    pn_edge_switch = ''
    pn_egress_rate_limit = ''
    pn_host = ''
    pn_jumbo = ''
    pn_lacp_fallback = ''
    pn_lacp_fallback_timeout = ''
    pn_lacp_mode = ''
    pn_lacp_priority = ''
    pn_lacp_timeout = ''
    pn_loopback = ''
    pn_loopvlans = ''
    pn_mirror_receive = ''
    pn_pause = ''
    pn_port_macaddr = ''
    pn_ports = ''
    pn_routing = ''
    pn_speed = ''
    pn_unknown_mcast_level = ''
    pn_unknown_ucast_level = ''
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

