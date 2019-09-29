import random
import string
import os
from register import registerObj
import writer

class bigiq_application_https_offload:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    password = ''
    server = ''
    user = ''
    add_analytics = ''
    client_ssl_profile = ''
    description = ''
    inbound_virtual = ''
    provider = ''
    redirect_virtual = ''
    server_port = ''
    servers = ''
    service_environment = ''
    state = ''
    validate_certs = ''
    wait = ''
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

