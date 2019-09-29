import random
import string
import os
from register import registerObj
import writer

class docker_image:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    api_version = ''
    archive_path = ''
    build = ''
    buildargs = ''
    ca_cert = ''
    client_cert = ''
    client_key = ''
    container_limits = ''
    debug = ''
    docker_host = ''
    dockerfile = ''
    force = ''
    force_absent = ''
    force_source = ''
    force_tag = ''
    http_timeout = ''
    load_path = ''
    nocache = ''
    path = ''
    pull = ''
    push = ''
    repository = ''
    rm = ''
    source = ''
    ssl_version = ''
    state = ''
    tag = ''
    timeout = ''
    tls = ''
    tls_hostname = ''
    use_tls = ''
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

