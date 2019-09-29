import random
import string
import os
from register import registerObj
import writer

class aci_bd:
    playbook_name = ''
    hosts=[]
    register=[]
    host = ''
    password = ''
    private_key = ''
    arp_flooding = ''
    bd = ''
    bd_type = ''
    certificate_name = ''
    description = ''
    enable_multicast = ''
    enable_routing = ''
    endpoint_clear = ''
    endpoint_move_detect = ''
    endpoint_retention_action = ''
    endpoint_retention_policy = ''
    igmp_snoop_policy = ''
    ip_learning = ''
    ipv6_nd_policy = ''
    l2_unknown_unicast = ''
    l3_unknown_multicast = ''
    limit_ip_learn = ''
    mac_address = ''
    multi_dest = ''
    output_level = ''
    port = ''
    state = ''
    tenant = ''
    timeout = ''
    use_proxy = ''
    use_ssl = ''
    username = ''
    validate_certs = ''
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

