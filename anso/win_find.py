import random
import string
import os
from register import registerObj
import writer

class win_find:
    playbook_name = ''
    hosts=[]
    register=[]
    paths = ''
    age = ''
    age_stamp = ''
    checksum_algorithm = ''
    file_type = ''
    follow = ''
    get_checksum = ''
    hidden = ''
    patterns = ''
    recurse = ''
    size = ''
    use_regex = ''
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

