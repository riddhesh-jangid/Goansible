import random
import string
import os
from register import registerObj
import writer

class scaleway_compute:
    playbook_name = ''
    hosts=[]
    register=[]
    commercial_type = ''
    image = ''
    organization = ''
    region = ''
    api_timeout = ''
    api_token = ''
    api_url = ''
    enable_ipv6 = ''
    name = ''
    public_ip = ''
    query_parameters = ''
    security_group = ''
    state = ''
    tags = ''
    validate_certs = ''
    wait = ''
    wait_sleep_time = ''
    wait_timeout = ''
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

