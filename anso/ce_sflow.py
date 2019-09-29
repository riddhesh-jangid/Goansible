import random
import string
import os
from register import registerObj
import writer

class ce_sflow:
    playbook_name = ''
    hosts=[]
    register=[]
    agent_ip = ''
    collector_datagram_size = ''
    collector_description = ''
    collector_id = ''
    collector_ip = ''
    collector_ip_vpn = ''
    collector_meth = ''
    collector_udp_port = ''
    counter_collector = ''
    counter_interval = ''
    export_route = ''
    forward_enp_slot = ''
    rate_limit = ''
    rate_limit_slot = ''
    sample_collector = ''
    sample_direction = ''
    sample_length = ''
    sample_rate = ''
    sflow_interface = ''
    source_ip = ''
    state = ''
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

