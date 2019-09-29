import random
import string
import os
from register import registerObj
import writer

class openshift_scale:
    playbook_name = ''
    hosts=[]
    register=[]
    api_key = ''
    api_version = ''
    ca_cert = ''
    client_cert = ''
    client_key = ''
    context = ''
    current_replicas = ''
    host = ''
    kind = ''
    kubeconfig = ''
    name = ''
    namespace = ''
    password = ''
    replicas = ''
    resource_definition = ''
    resource_version = ''
    src = ''
    username = ''
    validate_certs = ''
    wait = ''
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

