import random
import string
import os
from register import registerObj
import writer

class gcp_compute_instance:
    playbook_name = ''
    hosts=[]
    register=[]
    auth_kind = ''
    zone = ''
    can_ip_forward = ''
    disks = ''
    guest_accelerators = ''
    label_fingerprint = ''
    machine_type = ''
    metadata = ''
    min_cpu_platform = ''
    name = ''
    network_interfaces = ''
    project = ''
    scheduling = ''
    scopes = ''
    service_account_contents = ''
    service_account_email = ''
    service_account_file = ''
    service_accounts = ''
    state = ''
    status = ''
    tags = ''
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

