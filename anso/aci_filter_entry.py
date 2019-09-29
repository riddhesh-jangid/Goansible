import random
import string
import os
from register import registerObj
import writer

class aci_filter_entry:
    playbook_name = ''
    hosts=[]
    register=[]
    host = ''
    password = ''
    private_key = ''
    arp_flag = ''
    certificate_name = ''
    description = ''
    dst_port = ''
    dst_port_end = ''
    dst_port_start = ''
    entry = ''
    ether_type = ''
    filter = ''
    icmp6_msg_type = ''
    icmp_msg_type = ''
    ip_protocol = ''
    output_level = ''
    port = ''
    state = ''
    stateful = ''
    tenant = ''
    timeout = ''
    use_proxy = ''
    use_ssl = ''
    username = ''
    validate_certs = ''
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

