import random
import string
import os
from register import registerObj
import writer

class a10_virtual_server:
    playbook_name = ''
    hosts=[]
    register=[]
    host = ''
    password = ''
    username = ''
    virtual_server = ''
    client_cert = ''
    client_key = ''
    force = ''
    force_basic_auth = ''
    http_agent = ''
    partition = ''
    state = ''
    url = ''
    url_password = ''
    url_username = ''
    use_proxy = ''
    validate_certs = ''
    virtual_server_ip = ''
    virtual_server_ports = ''
    virtual_server_status = ''
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

