import random
import string
import os
from register import registerObj
import writer

class docker_swarm_info:
    playbook_name = ''
    hosts=[]
    register=[]
    api_version = ''
    ca_cert = ''
    client_cert = ''
    client_key = ''
    debug = ''
    docker_host = ''
    nodes = ''
    nodes_filters = ''
    services = ''
    services_filters = ''
    ssl_version = ''
    tasks = ''
    tasks_filters = ''
    timeout = ''
    tls = ''
    tls_hostname = ''
    unlock_key = ''
    validate_certs = ''
    verbose_output = ''
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

