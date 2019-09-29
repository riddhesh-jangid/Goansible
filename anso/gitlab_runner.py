import random
import string
import os
from register import registerObj
import writer

class gitlab_runner:
    playbook_name = ''
    hosts=[]
    register=[]
    api_token = ''
    description = ''
    registration_token = ''
    url = ''
    access_level = ''
    active = ''
    api_password = ''
    api_url = ''
    api_username = ''
    locked = ''
    maximum_timeout = ''
    run_untagged = ''
    state = ''
    tag_list = ''
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

