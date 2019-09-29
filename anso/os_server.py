import random
import string
import os
from register import registerObj
import writer

class os_server:
    playbook_name = ''
    hosts=[]
    register=[]
    image = ''
    name = ''
    api_timeout = ''
    auth = ''
    auth_type = ''
    auto_ip = ''
    availability_zone = ''
    boot_from_volume = ''
    boot_volume = ''
    ca_cert = ''
    client_cert = ''
    client_key = ''
    cloud = ''
    config_drive = ''
    delete_fip = ''
    flavor = ''
    flavor_include = ''
    flavor_ram = ''
    floating_ip_pools = ''
    floating_ips = ''
    image_exclude = ''
    interface = ''
    key_name = ''
    meta = ''
    network = ''
    nics = ''
    region_name = ''
    reuse_ips = ''
    scheduler_hints = ''
    security_groups = ''
    state = ''
    terminate_volume = ''
    timeout = ''
    userdata = ''
    validate_certs = ''
    volume_size = ''
    volumes = ''
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

