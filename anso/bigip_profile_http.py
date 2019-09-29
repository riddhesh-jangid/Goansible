import random
import string
import os
from register import registerObj
import writer

class bigip_profile_http:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    password = ''
    server = ''
    user = ''
    description = ''
    dns_resolver = ''
    encrypt_cookie_secret = ''
    encrypt_cookies = ''
    header_erase = ''
    header_insert = ''
    hsts_mode = ''
    include_subdomains = ''
    insert_xforwarded_for = ''
    maximum_age = ''
    parent = ''
    partition = ''
    provider = ''
    proxy_type = ''
    redirect_rewrite = ''
    server_agent_name = ''
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

