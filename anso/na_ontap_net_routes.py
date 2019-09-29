import random
import string
import os
from register import registerObj
import writer

class na_ontap_net_routes:
    playbook_name = ''
    hosts=[]
    register=[]
    destination = ''
    gateway = ''
    hostname = ''
    password = ''
    username = ''
    vserver = ''
    from_destination = ''
    from_gateway = ''
    from_metric = ''
    http_port = ''
    https = ''
    metric = ''
    ontapi = ''
    state = ''
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

