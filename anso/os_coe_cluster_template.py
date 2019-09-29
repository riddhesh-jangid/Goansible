import random
import string
import os
from register import registerObj
import writer

class os_coe_cluster_template:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    api_timeout = ''
    auth = ''
    auth_type = ''
    availability_zone = ''
    ca_cert = ''
    client_cert = ''
    client_key = ''
    cloud = ''
    coe = ''
    dns_nameserver = ''
    docker_storage_driver = ''
    docker_volume_size = ''
    external_network_id = ''
    fixed_network = ''
    fixed_subnet = ''
    flavor_id = ''
    floating_ip_enabled = ''
    http_proxy = ''
    https_proxy = ''
    image_id = ''
    interface = ''
    keypair_id = ''
    labels = ''
    master_flavor_id = ''
    master_lb_enabled = ''
    network_driver = ''
    no_proxy = ''
    public = ''
    region_name = ''
    registry_enabled = ''
    server_type = ''
    state = ''
    timeout = ''
    tls_disabled = ''
    validate_certs = ''
    volume_driver = ''
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

