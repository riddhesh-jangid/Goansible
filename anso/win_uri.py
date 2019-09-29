import random
import string
import os
from register import registerObj
import writer

class win_uri:
    playbook_name = ''
    hosts=[]
    register=[]
    url = ''
    body = ''
    client_cert = ''
    client_cert_password = ''
    content_type = ''
    creates = ''
    dest = ''
    follow_redirects = ''
    force_basic_auth = ''
    headers = ''
    maximum_redirection = ''
    method = ''
    password = ''
    removes = ''
    return_content = ''
    status_code = ''
    timeout = ''
    user = ''
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

