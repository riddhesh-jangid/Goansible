import random
import string
import os
from register import registerObj
import writer

class ce_vxlan_gateway:
    playbook_name = ''
    hosts=[]
    register=[]
    arp_direct_route = ''
    arp_distribute_gateway = ''
    dfs_all_active = ''
    dfs_id = ''
    dfs_peer_ip = ''
    dfs_peer_vpn = ''
    dfs_source_ip = ''
    dfs_source_vpn = ''
    dfs_udp_port = ''
    state = ''
    vbdif_bind_vpn = ''
    vbdif_mac = ''
    vbdif_name = ''
    vpn_instance = ''
    vpn_vni = ''
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

