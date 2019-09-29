import random
import string
import os
from register import registerObj
import writer

class pn_port_config:
    playbook_name = ''
    hosts=[]
    register=[]
    state = ''
    pn_allowed_tpid = ''
    pn_autoneg = ''
    pn_cliswitch = ''
    pn_crc_check_enable = ''
    pn_defer_bringup = ''
    pn_description = ''
    pn_dscp_map = ''
    pn_edge_switch = ''
    pn_egress_rate_limit = ''
    pn_enable = ''
    pn_eth_mode = ''
    pn_fabric_guard = ''
    pn_host_enable = ''
    pn_intf = ''
    pn_jumbo = ''
    pn_lacp_priority = ''
    pn_local_switching = ''
    pn_loop_vlans = ''
    pn_loopback = ''
    pn_mirror_only = ''
    pn_pause = ''
    pn_port = ''
    pn_port_mac_address = ''
    pn_reflect = ''
    pn_routing = ''
    pn_send_port = ''
    pn_speed = ''
    pn_vxlan_termination = ''
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

