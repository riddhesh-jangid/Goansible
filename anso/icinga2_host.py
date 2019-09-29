import random
import string
import os
from register import registerObj
import writer

class icinga2_host:
    playbook_name = ''
    hosts=[]
    register=[]
    ip = ''
    name = ''
    url = ''
    check_command = ''
    client_cert = ''
    client_key = ''
    display_name = ''
    force_basic_auth = ''
    state = ''
    template = ''
    url_password = ''
    url_username = ''
    use_proxy = ''
    validate_certs = ''
    variables = ''
    zone = ''
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

