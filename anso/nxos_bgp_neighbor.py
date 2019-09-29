import random
import string
import os
from register import registerObj
import writer

class nxos_bgp_neighbor:
    playbook_name = ''
    hosts=[]
    register=[]
    asn = ''
    neighbor = ''
    capability_negotiation = ''
    connected_check = ''
    description = ''
    dynamic_capability = ''
    ebgp_multihop = ''
    local_as = ''
    log_neighbor_changes = ''
    low_memory_exempt = ''
    maximum_peers = ''
    provider = ''
    pwd = ''
    pwd_type = ''
    remote_as = ''
    remove_private_as = ''
    shutdown = ''
    state = ''
    suppress_4_byte_as = ''
    timers_holdtime = ''
    timers_keepalive = ''
    transport_passive_only = ''
    update_source = ''
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

