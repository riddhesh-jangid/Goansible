import random
import string
import os
from register import registerObj
import writer

class ce_bgp:
    playbook_name = ''
    hosts=[]
    register=[]
    as_number = ''
    as_path_limit = ''
    bgp_rid_auto_sel = ''
    check_first_as = ''
    clear_interval = ''
    confed_id_number = ''
    confed_nonstanded = ''
    confed_peer_as_num = ''
    conn_retry_time = ''
    default_af_type = ''
    ebgp_if_sensitive = ''
    gr_peer_reset = ''
    graceful_restart = ''
    hold_interval = ''
    hold_time = ''
    is_shutdown = ''
    keep_all_routes = ''
    keepalive_time = ''
    memory_limit = ''
    min_hold_time = ''
    router_id = ''
    state = ''
    suppress_interval = ''
    time_wait_for_rib = ''
    vrf_name = ''
    vrf_rid_auto_sel = ''
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

