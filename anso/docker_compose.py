import random
import string
import os
from register import registerObj
import writer

class docker_compose:
    playbook_name = ''
    hosts=[]
    register=[]
    api_version = ''
    build = ''
    ca_cert = ''
    client_cert = ''
    client_key = ''
    debug = ''
    definition = ''
    dependencies = ''
    docker_host = ''
    files = ''
    hostname_check = ''
    nocache = ''
    project_name = ''
    project_src = ''
    pull = ''
    recreate = ''
    remove_images = ''
    remove_orphans = ''
    remove_volumes = ''
    restarted = ''
    scale = ''
    services = ''
    ssl_version = ''
    state = ''
    stopped = ''
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

