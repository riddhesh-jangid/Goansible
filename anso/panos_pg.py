import random
import string
import os
from register import registerObj
import writer

class panos_pg:
    playbook_name = ''
    hosts=[]
    register=[]
    ip_address = ''
    password = ''
    pg_name = ''
    commit = ''
    data_filtering = ''
    file_blocking = ''
    spyware = ''
    url_filtering = ''
    username = ''
    virus = ''
    vulnerability = ''
    wildfire = ''
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

