import random
import string
import os
from register import registerObj
import writer

class oneandone_server:
    playbook_name = ''
    hosts=[]
    register=[]
    auth_token = ''
    fixed_instance_size = ''
    api_url = ''
    appliance = ''
    auto_increment = ''
    cores_per_processor = ''
    count = ''
    datacenter = ''
    description = ''
    firewall_policy = ''
    hdds = ''
    hostname = ''
    load_balancer = ''
    monitoring_policy = ''
    private_network = ''
    ram = ''
    server = ''
    server_type = ''
    ssh_key = ''
    state = ''
    vcore = ''
    wait = ''
    wait_interval = ''
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

