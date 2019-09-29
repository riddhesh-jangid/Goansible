import random
import string
import os
from register import registerObj
import writer

class manageiq_alert_profiles:
    playbook_name = ''
    hosts=[]
    register=[]
    manageiq_connection = ''
    alerts = ''
    name = ''
    notes = ''
    resource_type = ''
    state = ''
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

