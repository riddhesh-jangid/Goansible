import random
import string
import os
from register import registerObj
import writer

class nmcli:
    playbook_name = ''
    hosts=[]
    register=[]
    conn_name = ''
    state = ''
    ageingtime = ''
    arp_interval = ''
    arp_ip_target = ''
    autoconnect = ''
    dhcp_client_id = ''
    dns4 = ''
    dns4_search = ''
    dns6 = ''
    dns6_search = ''
    downdelay = ''
    egress = ''
    flags = ''
    forwarddelay = ''
    gw4 = ''
    gw6 = ''
    hairpin = ''
    hellotime = ''
    ifname = ''
    ingress = ''
    ip4 = ''
    ip6 = ''
    ip_tunnel_dev = ''
    ip_tunnel_local = ''
    ip_tunnel_remote = ''
    mac = ''
    master = ''
    maxage = ''
    miimon = ''
    mode = ''
    mtu = ''
    path_cost = ''
    primary = ''
    priority = ''
    slavepriority = ''
    stp = ''
    type = ''
    updelay = ''
    vlandev = ''
    vlanid = ''
    vxlan_id = ''
    vxlan_local = ''
    vxlan_remote = ''
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

