import random
import string
import os
from register import registerObj
import writer

class os_coe_cluster:
    playbook_name = ''
    hosts=[]
    register=[]
    cluster_template_id = ''
    name = ''
    api_timeout = ''
    auth = ''
    auth_type = ''
    availability_zone = ''
    ca_cert = ''
    client_cert = ''
    client_key = ''
    cloud = ''
    discovery_url = ''
    docker_volume_size = ''
    flavor_id = ''
    interface = ''
    keypair = ''
    labels = ''
    master_count = ''
    master_flavor_id = ''
    node_count = ''
    region_name = ''
    state = ''
    timeout = ''
    validate_certs = ''
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

