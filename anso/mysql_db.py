import random
import string
import os
from register import registerObj
import writer

class mysql_db:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    ca_cert = ''
    client_cert = ''
    client_key = ''
    collation = ''
    config_file = ''
    connect_timeout = ''
    encoding = ''
    ignore_tables = ''
    login_host = ''
    login_password = ''
    login_port = ''
    login_unix_socket = ''
    login_user = ''
    quick = ''
    single_transaction = ''
    state = ''
    target = ''
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

