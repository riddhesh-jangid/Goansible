import random
import string
import os
from register import registerObj
import writer

class fmgr_query:
    playbook_name = ''
    hosts=[]
    register=[]
    object = ''
    adom = ''
    custom_dict = ''
    custom_endpoint = ''
    device_ip = ''
    device_serial = ''
    device_unique_name = ''
    nodes = ''
    task_id = ''
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

