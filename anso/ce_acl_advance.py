import random
import string
import os
from register import registerObj
import writer

class ce_acl_advance:
    playbook_name = ''
    hosts=[]
    register=[]
    acl_name = ''
    acl_description = ''
    acl_num = ''
    acl_step = ''
    dest_ip = ''
    dest_mask = ''
    dest_pool_name = ''
    dest_port_begin = ''
    dest_port_end = ''
    dest_port_op = ''
    dest_port_pool_name = ''
    dscp = ''
    established = ''
    frag_type = ''
    icmp_code = ''
    icmp_name = ''
    icmp_type = ''
    igmp_type = ''
    log_flag = ''
    precedence = ''
    protocol = ''
    rule_action = ''
    rule_description = ''
    rule_id = ''
    rule_name = ''
    source_ip = ''
    src_mask = ''
    src_pool_name = ''
    src_port_begin = ''
    src_port_end = ''
    src_port_op = ''
    src_port_pool_name = ''
    state = ''
    syn_flag = ''
    tcp_flag_mask = ''
    time_range = ''
    tos = ''
    ttl_expired = ''
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

