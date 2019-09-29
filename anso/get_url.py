import random
import string
import os
from register import registerObj
import writer

class get_url:
    playbook_name = ''
    hosts=[]
    register=[]
    dest = ''
    url = ''
    attributes = ''
    backup = ''
    checksum = ''
    client_cert = ''
    client_key = ''
    force = ''
    force_basic_auth = ''
    group = ''
    headers = ''
    http_agent = ''
    mode = ''
    owner = ''
    selevel = ''
    serole = ''
    setype = ''
    seuser = ''
    sha256sum = ''
    timeout = ''
    tmp_dest = ''
    unsafe_writes = ''
    url_password = ''
    url_username = ''
    use_proxy = ''
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

