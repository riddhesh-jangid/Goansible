import random
import string
import os
from register import registerObj
import writer

class cli_config:
    playbook_name = ''
    hosts=[]
    register=[]
    backup = ''
    backup_options = ''
    commit = ''
    commit_comment = ''
    config = ''
    defaults = ''
    diff_ignore_lines = ''
    diff_match = ''
    diff_replace = ''
    multiline_delimiter = ''
    replace = ''
    rollback = ''
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

