import random
import string
import os
from register import registerObj
import writer

class tower_workflow_template:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    allow_simultaneous = ''
    description = ''
    extra_vars = ''
    organization = ''
    schema = ''
    state = ''
    survey = ''
    survey_enabled = ''
    tower_config_file = ''
    tower_host = ''
    tower_password = ''
    tower_username = ''
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

