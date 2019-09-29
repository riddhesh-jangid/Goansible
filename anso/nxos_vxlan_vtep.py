import random
import string
import os
from register import registerObj
import writer

class nxos_vxlan_vtep:
    playbook_name = ''
    hosts=[]
    register=[]
    interface = ''
    description = ''
    global_ingress_replication_bgp = ''
    global_mcast_group_L2 = ''
    global_mcast_group_L3 = ''
    global_suppress_arp = ''
    host_reachability = ''
    provider = ''
    shutdown = ''
    source_interface = ''
    source_interface_hold_down_time = ''
    state = ''
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

