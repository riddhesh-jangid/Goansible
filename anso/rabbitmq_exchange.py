import random
import string
import os
from register import registerObj
import writer

class rabbitmq_exchange:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    arguments = ''
    auto_delete = ''
    ca_cert = ''
    client_cert = ''
    client_key = ''
    durable = ''
    exchange_type = ''
    internal = ''
    login_host = ''
    login_password = ''
    login_port = ''
    login_protocol = ''
    login_user = ''
    state = ''
    vhost = ''
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

