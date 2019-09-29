import random
import string
import os
from register import registerObj
import writer

class clc_server:
    playbook_name = ''
    hosts=[]
    register=[]
    add_public_ip = ''
    additional_disks = ''
    alert_policy_id = ''
    alert_policy_name = ''
    alias = ''
    anti_affinity_policy_id = ''
    anti_affinity_policy_name = ''
    configuration_id = ''
    count = ''
    count_group = ''
    cpu = ''
    cpu_autoscale_policy_id = ''
    custom_fields = ''
    description = ''
    exact_count = ''
    group = ''
    ip_address = ''
    location = ''
    managed_os = ''
    memory = ''
    name = ''
    network_id = ''
    os_type = ''
    packages = ''
    password = ''
    primary_dns = ''
    public_ip_ports = ''
    public_ip_protocol = ''
    secondary_dns = ''
    server_ids = ''
    source_server_password = ''
    state = ''
    storage_type = ''
    template = ''
    ttl = ''
    type = ''
    wait = ''
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

