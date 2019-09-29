import random
import string
import os
from register import registerObj
import writer

class zabbix_proxy:
    playbook_name = ''
    hosts=[]
    register=[]
    http_login_user = ''
    login_password = ''
    login_user = ''
    proxy_name = ''
    server_url = ''
    ca_cert = ''
    description = ''
    http_login_password = ''
    interface = ''
    state = ''
    status = ''
    timeout = ''
    tls_accept = ''
    tls_connect = ''
    tls_psk = ''
    tls_psk_identity = ''
    tls_subject = ''
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

