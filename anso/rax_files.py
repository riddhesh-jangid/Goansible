import random
import string
import os
from register import registerObj
import writer

class rax_files:
    playbook_name = ''
    hosts=[]
    register=[]
    container = ''
    api_key = ''
    auth_endpoint = ''
    clear_meta = ''
    credentials = ''
    env = ''
    identity_type = ''
    meta = ''
    private = ''
    public = ''
    region = ''
    state = ''
    tenant_id = ''
    tenant_name = ''
    ttl = ''
    type = ''
    username = ''
    validate_certs = ''
    web_error = ''
    web_index = ''
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

