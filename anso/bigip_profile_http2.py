import random
import string
import os
from register import registerObj
import writer

class bigip_profile_http2:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    password = ''
    server = ''
    user = ''
    activation_modes = ''
    description = ''
    enforce_tls_requirements = ''
    frame_size = ''
    header_table_size = ''
    idle_timeout = ''
    insert_header = ''
    insert_header_name = ''
    parent = ''
    partition = ''
    provider = ''
    receive_window = ''
    server_port = ''
    state = ''
    streams = ''
    validate_certs = ''
    write_size = ''
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

