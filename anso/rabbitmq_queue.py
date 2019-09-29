import random
import string
import os
from register import registerObj
import writer

class rabbitmq_queue:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    arguments = ''
    auto_delete = ''
    auto_expires = ''
    ca_cert = ''
    client_cert = ''
    client_key = ''
    dead_letter_exchange = ''
    dead_letter_routing_key = ''
    durable = ''
    login_host = ''
    login_password = ''
    login_port = ''
    login_protocol = ''
    login_user = ''
    max_length = ''
    max_priority = ''
    message_ttl = ''
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

