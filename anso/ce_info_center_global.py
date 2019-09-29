import random
import string
import os
from register import registerObj
import writer

class ce_info_center_global:
    playbook_name = ''
    hosts=[]
    register=[]
    channel_cfg_name = ''
    channel_id = ''
    channel_name = ''
    channel_out_direct = ''
    facility = ''
    filter_feature_name = ''
    filter_log_name = ''
    info_center_enable = ''
    ip_type = ''
    is_default_vpn = ''
    level = ''
    logfile_max_num = ''
    logfile_max_size = ''
    packet_priority = ''
    server_domain = ''
    server_ip = ''
    server_port = ''
    source_ip = ''
    ssl_policy_name = ''
    state = ''
    suppress_enable = ''
    timestamp = ''
    transport_mode = ''
    vrf_name = ''
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

