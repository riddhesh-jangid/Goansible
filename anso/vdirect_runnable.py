import random
import string
import os
from register import registerObj
import writer

class vdirect_runnable:
    playbook_name = ''
    hosts=[]
    register=[]
    runnable_name = ''
    runnable_type = ''
    vdirect_ip = ''
    vdirect_password = ''
    vdirect_user = ''
    action_name = ''
    parameters = ''
    validate_certs = ''
    vdirect_http_port = ''
    vdirect_https_port = ''
    vdirect_secondary_ip = ''
    vdirect_timeout = ''
    vdirect_use_ssl = ''
    vdirect_wait = ''
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

