import random
import string
import os
from register import registerObj
import writer

class nxos_file_copy:
    playbook_name = ''
    hosts=[]
    register=[]
    connect_ssh_port = ''
    file_pull = ''
    file_pull_timeout = ''
    file_system = ''
    local_file = ''
    local_file_directory = ''
    provider = ''
    remote_file = ''
    remote_scp_server = ''
    remote_scp_server_password = ''
    remote_scp_server_user = ''
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

