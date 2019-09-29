import random
import string
import os
from register import registerObj
import writer

class tower_credential:
    playbook_name = ''
    hosts=[]
    register=[]
    kind = ''
    name = ''
    organization = ''
    authorize = ''
    authorize_password = ''
    become_method = ''
    become_password = ''
    become_username = ''
    client = ''
    description = ''
    domain = ''
    host = ''
    password = ''
    project = ''
    secret = ''
    security_token = ''
    ssh_key_data = ''
    ssh_key_unlock = ''
    state = ''
    subscription = ''
    team = ''
    tenant = ''
    tower_config_file = ''
    tower_host = ''
    tower_password = ''
    tower_username = ''
    user = ''
    username = ''
    validate_certs = ''
    vault_id = ''
    vault_password = ''
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

