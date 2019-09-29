import random
import string
import os
from register import registerObj
import writer

class jenkins_plugin:
    playbook_name = ''
    hosts=[]
    register=[]
    client_cert = ''
    client_key = ''
    force = ''
    force_basic_auth = ''
    group = ''
    http_agent = ''
    jenkins_home = ''
    mode = ''
    name = ''
    owner = ''
    state = ''
    timeout = ''
    updates_expiration = ''
    updates_url = ''
    url = ''
    url_password = ''
    url_username = ''
    use_proxy = ''
    validate_certs = ''
    version = ''
    with_dependencies = ''
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

