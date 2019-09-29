import random
import string
import os
from register import registerObj
import writer

class nxos_bgp_af:
    playbook_name = ''
    hosts=[]
    register=[]
    afi = ''
    asn = ''
    safi = ''
    vrf = ''
    additional_paths_install = ''
    additional_paths_receive = ''
    additional_paths_selection = ''
    additional_paths_send = ''
    advertise_l2vpn_evpn = ''
    client_to_client = ''
    dampen_igp_metric = ''
    dampening_half_time = ''
    dampening_max_suppress_time = ''
    dampening_reuse_time = ''
    dampening_routemap = ''
    dampening_state = ''
    dampening_suppress_time = ''
    default_information_originate = ''
    default_metric = ''
    distance_ebgp = ''
    distance_ibgp = ''
    distance_local = ''
    inject_map = ''
    maximum_paths = ''
    maximum_paths_ibgp = ''
    networks = ''
    next_hop_route_map = ''
    provider = ''
    redistribute = ''
    state = ''
    suppress_inactive = ''
    table_map = ''
    table_map_filter = ''
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

