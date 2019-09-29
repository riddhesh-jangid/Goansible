import random
import string
import os
from register import registerObj
import writer

class gcp_url_map:
    playbook_name = ''
    hosts=[]
    register=[]
    default_service = ''
    url_map_name = ''
    host_rules = ''
    path_matchers = ''
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

