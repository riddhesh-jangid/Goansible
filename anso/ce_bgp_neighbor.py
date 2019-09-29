import random
import string
import os
from register import registerObj
import writer

class ce_bgp_neighbor:
    playbook_name = ''
    hosts=[]
    register=[]
    peer_addr = ''
    remote_as = ''
    vrf_name = ''
    conn_retry_time = ''
    connect_mode = ''
    conventional = ''
    description = ''
    dual_as = ''
    ebgp_max_hop = ''
    fake_as = ''
    hold_time = ''
    is_bfd_block = ''
    is_bfd_enable = ''
    is_ignore = ''
    is_log_change = ''
    is_single_hop = ''
    keep_alive_time = ''
    key_chain_name = ''
    local_if_name = ''
    min_hold_time = ''
    mpls_local_ifnet_disable = ''
    multiplier = ''
    prepend_fake_as = ''
    prepend_global_as = ''
    pswd_cipher_text = ''
    pswd_type = ''
    route_refresh = ''
    rx_interval = ''
    state = ''
    tcp_MSS = ''
    tx_interval = ''
    valid_ttl_hops = ''
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

