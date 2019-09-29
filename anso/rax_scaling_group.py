import random
import string
import os
from register import registerObj
import writer

class rax_scaling_group:
    playbook_name = ''
    hosts=[]
    register=[]
    flavor = ''
    image = ''
    max_entities = ''
    min_entities = ''
    name = ''
    server_name = ''
    api_key = ''
    auth_endpoint = ''
    config_drive = ''
    cooldown = ''
    credentials = ''
    disk_config = ''
    env = ''
    files = ''
    identity_type = ''
    key_name = ''
    loadbalancers = ''
    meta = ''
    networks = ''
    region = ''
    state = ''
    tenant_id = ''
    tenant_name = ''
    user_data = ''
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

