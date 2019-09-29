import random
import string
import os
from register import registerObj
import writer

class bigip_device_httpd:
    playbook_name = ''
    hosts=[]
    register=[]
    password = ''
    server = ''
    user = ''
    allow = ''
    auth_name = ''
    auth_pam_dashboard_timeout = ''
    auth_pam_idle_timeout = ''
    auth_pam_validate_ip = ''
    fast_cgi_timeout = ''
    hostname_lookup = ''
    log_level = ''
    max_clients = ''
    provider = ''
    redirect_http_to_https = ''
    server_port = ''
    ssl_cipher_suite = ''
    ssl_port = ''
    ssl_protocols = ''
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

