import random
import string
import os
from register import registerObj
import writer

class idrac_firmware:
    playbook_name = ''
    hosts=[]
    register=[]
    idrac_ip = ''
    idrac_password = ''
    idrac_user = ''
    share_mnt = ''
    share_name = ''
    catalog_file_name = ''
    idrac_port = ''
    job_wait = ''
    reboot = ''
    share_password = ''
    share_user = ''
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

