import random
import string
import os
from register import registerObj
import writer

class docker_network:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    api_version = ''
    appends = ''
    attachable = ''
    ca_cert = ''
    client_cert = ''
    client_key = ''
    connected = ''
    debug = ''
    docker_host = ''
    driver = ''
    driver_options = ''
    enable_ipv6 = ''
    force = ''
    internal = ''
    ipam_config = ''
    ipam_driver = ''
    ipam_driver_options = ''
    ipam_options = ''
    labels = ''
    scope = ''
    ssl_version = ''
    state = ''
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

