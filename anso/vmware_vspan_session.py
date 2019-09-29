import random
import string
import os
from register import registerObj
import writer

class vmware_vspan_session:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    state = ''
    switch = ''
    description = ''
    destination_port = ''
    destination_vm = ''
    enabled = ''
    encapsulation_vlan_id = ''
    hostname = ''
    mirrored_packet_length = ''
    normal_traffic_allowed = ''
    password = ''
    port = ''
    sampling_rate = ''
    session_type = ''
    source_port_received = ''
    source_port_transmitted = ''
    source_vm_received = ''
    source_vm_transmitted = ''
    strip_original_vlan = ''
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

