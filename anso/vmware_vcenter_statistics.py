import random
import string
import os
from register import registerObj
import writer

class vmware_vcenter_statistics:
    playbook_name = ''
    hosts=[]
    register=[]
    hostname = ''
    interval_past_day = ''
    interval_past_month = ''
    interval_past_week = ''
    interval_past_year = ''
    password = ''
    port = ''
    username = ''
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

