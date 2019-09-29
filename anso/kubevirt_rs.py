import random
import string
import os
from register import registerObj
import writer

class kubevirt_rs:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    namespace = ''
    selector = ''
    api_key = ''
    bootloader = ''
    ca_cert = ''
    client_cert = ''
    client_key = ''
    cloud_init_nocloud = ''
    context = ''
    cpu_cores = ''
    cpu_features = ''
    cpu_limit = ''
    cpu_model = ''
    cpu_shares = ''
    disks = ''
    force = ''
    headless = ''
    host = ''
    hugepage_size = ''
    interfaces = ''
    kubeconfig = ''
    labels = ''
    machine_type = ''
    memory = ''
    memory_limit = ''
    merge_type = ''
    password = ''
    replicas = ''
    resource_definition = ''
    smbios_uuid = ''
    state = ''
    tablets = ''
    username = ''
    validate_certs = ''
    wait = ''
    wait_timeout = ''
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

