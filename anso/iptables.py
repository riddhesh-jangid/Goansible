import random
import string
import os
from register import registerObj
import writer

class iptables:
    playbook_name = ''
    hosts=[]
    register=[]
    action = ''
    chain = ''
    comment = ''
    ctstate = ''
    destination = ''
    destination_port = ''
    dst_range = ''
    flush = ''
    fragment = ''
    gateway = ''
    goto = ''
    icmp_type = ''
    in_interface = ''
    ip_version = ''
    jump = ''
    limit = ''
    limit_burst = ''
    log_level = ''
    log_prefix = ''
    match = ''
    out_interface = ''
    policy = ''
    protocol = ''
    reject_with = ''
    rule_num = ''
    set_counters = ''
    set_dscp_mark = ''
    set_dscp_mark_class = ''
    source = ''
    source_port = ''
    src_range = ''
    state = ''
    syn = ''
    table = ''
    tcp_flags = ''
    to_destination = ''
    to_ports = ''
    to_source = ''
    uid_owner = ''
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

