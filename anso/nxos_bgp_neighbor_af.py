import random
import string
import os
from register import registerObj
import writer

class nxos_bgp_neighbor_af:
    playbook_name = ''
    hosts=[]
    register=[]
    afi = ''
    asn = ''
    neighbor = ''
    safi = ''
    additional_paths_receive = ''
    additional_paths_send = ''
    advertise_map_exist = ''
    advertise_map_non_exist = ''
    allowas_in = ''
    allowas_in_max = ''
    as_override = ''
    default_originate = ''
    default_originate_route_map = ''
    disable_peer_as_check = ''
    filter_list_in = ''
    filter_list_out = ''
    max_prefix_interval = ''
    max_prefix_limit = ''
    max_prefix_threshold = ''
    max_prefix_warning = ''
    next_hop_self = ''
    next_hop_third_party = ''
    prefix_list_in = ''
    prefix_list_out = ''
    provider = ''
    route_map_in = ''
    route_map_out = ''
    route_reflector_client = ''
    send_community = ''
    soft_reconfiguration_in = ''
    soo = ''
    state = ''
    suppress_inactive = ''
    unsuppress_map = ''
    vrf = ''
    weight = ''
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

