import random
import string
import os
from register import registerObj
import writer

class rax_scaling_policy:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    policy_type = ''
    scaling_group = ''
    api_key = ''
    at = ''
    auth_endpoint = ''
    change = ''
    cooldown = ''
    credentials = ''
    cron = ''
    desired_capacity = ''
    env = ''
    identity_type = ''
    is_percent = ''
    region = ''
    state = ''
    tenant_id = ''
    tenant_name = ''
    username = ''
    validate_certs = ''
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

