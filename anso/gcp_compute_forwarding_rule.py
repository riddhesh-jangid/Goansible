import random
import string
import os
from register import registerObj
import writer

class gcp_compute_forwarding_rule:
    playbook_name = ''
    hosts=[]
    register=[]
    auth_kind = ''
    name = ''
    region = ''
    all_ports = ''
    backend_service = ''
    description = ''
    ip_address = ''
    ip_protocol = ''
    ip_version = ''
    load_balancing_scheme = ''
    network = ''
    network_tier = ''
    port_range = ''
    ports = ''
    project = ''
    scopes = ''
    service_account_contents = ''
    service_account_email = ''
    service_account_file = ''
    service_label = ''
    state = ''
    subnetwork = ''
    target = ''
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

