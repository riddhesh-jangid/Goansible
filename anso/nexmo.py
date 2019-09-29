import random
import string
import os
from register import registerObj
import writer

class nexmo:
    playbook_name = ''
    hosts=[]
    register=[]
    api_key = ''
    api_secret = ''
    dest = ''
    msg = ''
    src = ''
    client_cert = ''
    client_key = ''
    force = ''
    force_basic_auth = ''
    http_agent = ''
    url = ''
    url_password = ''
    url_username = ''
    use_proxy = ''
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

