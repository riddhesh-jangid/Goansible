import random
import string
import os
from register import registerObj
import writer

class rax:
    playbook_name = ''
    hosts=[]
    register=[]
    api_key = ''
    auth_endpoint = ''
    auto_increment = ''
    boot_from_volume = ''
    boot_volume = ''
    boot_volume_size = ''
    boot_volume_terminate = ''
    config_drive = ''
    count = ''
    count_offset = ''
    credentials = ''
    disk_config = ''
    env = ''
    exact_count = ''
    extra_client_args = ''
    extra_create_args = ''
    files = ''
    flavor = ''
    group = ''
    identity_type = ''
    image = ''
    instance_ids = ''
    key_name = ''
    meta = ''
    name = ''
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

