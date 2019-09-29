import random
import string
import os
from register import registerObj
import writer

class win_get_url:
    playbook_name = ''
    hosts=[]
    register=[]
    dest = ''
    url = ''
    checksum = ''
    checksum_algorithm = ''
    checksum_url = ''
    force = ''
    force_basic_auth = ''
    headers = ''
    proxy_password = ''
    proxy_url = ''
    proxy_username = ''
    timeout = ''
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

