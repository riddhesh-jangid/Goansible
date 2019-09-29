import random
import string
import os
from register import registerObj
import writer

class docker_node:
    playbook_name = ''
    hosts=[]
    register=[]
    hostname = ''
    api_version = ''
    availability = ''
    ca_cert = ''
    client_cert = ''
    client_key = ''
    debug = ''
    docker_host = ''
    labels = ''
    labels_state = ''
    labels_to_remove = ''
    role = ''
    ssl_version = ''
    timeout = ''
    tls = ''
    tls_hostname = ''
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

