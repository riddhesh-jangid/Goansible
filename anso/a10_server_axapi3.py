import random
import string
import os
from register import registerObj
import writer

class a10_server_axapi3:
    playbook_name = ''
    hosts=[]
    register=[]
    host = ''
    password = ''
    server_ip = ''
    server_name = ''
    username = ''
    client_cert = ''
    client_key = ''
    force = ''
    force_basic_auth = ''
    http_agent = ''
    operation = ''
    server_ports = ''
    server_status = ''
    url = ''
    url_password = ''
    url_username = ''
    use_proxy = ''
    validate_certs = ''
    write_config = ''
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

