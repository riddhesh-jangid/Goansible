import random
import string
import os
from register import registerObj
import writer

class mysql_replication:
    playbook_name = ''
    hosts=[]
    register=[]
    ca_cert = ''
    client_cert = ''
    client_key = ''
    config_file = ''
    connect_timeout = ''
    login_host = ''
    login_password = ''
    login_port = ''
    login_unix_socket = ''
    login_user = ''
    master_auto_position = ''
    master_connect_retry = ''
    master_host = ''
    master_log_file = ''
    master_log_pos = ''
    master_password = ''
    master_port = ''
    master_ssl = ''
    master_ssl_ca = ''
    master_ssl_capath = ''
    master_ssl_cert = ''
    master_ssl_cipher = ''
    master_ssl_key = ''
    master_user = ''
    mode = ''
    relay_log_file = ''
    relay_log_pos = ''
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

