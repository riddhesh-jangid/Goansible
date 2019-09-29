import random
import string
import os
from register import registerObj
import writer

class os_quota:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    api_timeout = ''
    auth = ''
    auth_type = ''
    availability_zone = ''
    backup_gigabytes = ''
    backups = ''
    ca_cert = ''
    client_cert = ''
    client_key = ''
    cloud = ''
    cores = ''
    fixed_ips = ''
    floating_ips = ''
    floatingip = ''
    gigabytes = ''
    gigabytes_lvm = ''
    injected_file_size = ''
    injected_files = ''
    injected_path_size = ''
    instances = ''
    interface = ''
    key_pairs = ''
    loadbalancer = ''
    network = ''
    per_volume_gigabytes = ''
    pool = ''
    port = ''
    properties = ''
    ram = ''
    rbac_policy = ''
    region_name = ''
    router = ''
    security_group = ''
    security_group_rule = ''
    server_group_members = ''
    server_groups = ''
    snapshots = ''
    snapshots_lvm = ''
    state = ''
    subnet = ''
    subnetpool = ''
    timeout = ''
    validate_certs = ''
    volumes = ''
    volumes_lvm = ''
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

