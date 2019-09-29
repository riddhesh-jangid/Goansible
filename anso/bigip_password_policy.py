import random
import string
import os
from register import registerObj
import writer

class bigip_password_policy:
    playbook_name = ''
    hosts=[]
    register=[]
    password = ''
    server = ''
    user = ''
    expiration_warning = ''
    max_duration = ''
    max_login_failures = ''
    min_duration = ''
    min_length = ''
    password_memory = ''
    policy_enforcement = ''
    provider = ''
    required_lowercase = ''
    required_numeric = ''
    required_special = ''
    required_uppercase = ''
    server_port = ''
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

