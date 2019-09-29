import random
import string
import os
from register import registerObj
import writer

class cs_instance_nic:
    playbook_name = ''
    hosts=[]
    register=[]
    network = ''
    vm = ''
    account = ''
    api_http_method = ''
    api_key = ''
    api_region = ''
    api_secret = ''
    api_timeout = ''
    api_url = ''
    domain = ''
    ip_address = ''
    poll_async = ''
    project = ''
    state = ''
    vpc = ''
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

