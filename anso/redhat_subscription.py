import random
import string
import os
from register import registerObj
import writer

class redhat_subscription:
    playbook_name = ''
    hosts=[]
    register=[]
    activationkey = ''
    auto_attach = ''
    consumer_id = ''
    consumer_name = ''
    consumer_type = ''
    environment = ''
    force_register = ''
    org_id = ''
    password = ''
    pool = ''
    pool_ids = ''
    release = ''
    rhsm_baseurl = ''
    rhsm_repo_ca_cert = ''
    server_hostname = ''
    server_insecure = ''
    server_proxy_hostname = ''
    server_proxy_password = ''
    server_proxy_port = ''
    server_proxy_user = ''
    state = ''
    username = ''
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

