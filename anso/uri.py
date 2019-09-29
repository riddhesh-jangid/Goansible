import random
import string
import os
from register import registerObj
import writer

class uri:
    playbook_name = ''
    hosts=[]
    register=[]
    url = ''
    HEADER_ = ''
    body = ''
    body_format = ''
    client_cert = ''
    client_key = ''
    creates = ''
    dest = ''
    follow_redirects = ''
    force = ''
    force_basic_auth = ''
    headers = ''
    http_agent = ''
    method = ''
    others = ''
    remote_src = ''
    removes = ''
    return_content = ''
    src = ''
    status_code = ''
    timeout = ''
    unix_socket = ''
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

