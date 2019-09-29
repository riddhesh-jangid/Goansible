import random
import string
import os
from register import registerObj
import writer

class bigip_profile_persistence_cookie:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    password = ''
    server = ''
    user = ''
    always_send = ''
    cookie_encryption = ''
    cookie_method = ''
    cookie_name = ''
    description = ''
    encrypt_cookie_pool_name = ''
    encryption_passphrase = ''
    expiration = ''
    http_only = ''
    match_across_pools = ''
    match_across_services = ''
    match_across_virtuals = ''
    override_connection_limit = ''
    parent = ''
    partition = ''
    provider = ''
    secure = ''
    server_port = ''
    state = ''
    update_password = ''
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

