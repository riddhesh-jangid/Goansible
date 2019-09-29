import random
import string
import os
from register import registerObj
import writer

class purefb_fs:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    api_token = ''
    eradicate = ''
    fastremove = ''
    fb_url = ''
    hard_limit = ''
    http = ''
    nfs = ''
    nfs_rules = ''
    size = ''
    smb = ''
    snapshot = ''
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

