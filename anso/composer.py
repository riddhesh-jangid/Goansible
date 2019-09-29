import random
import string
import os
from register import registerObj
import writer

class composer:
    playbook_name = ''
    hosts=[]
    register=[]
    apcu_autoloader = ''
    arguments = ''
    classmap_authoritative = ''
    command = ''
    executable = ''
    global_command = ''
    ignore_platform_reqs = ''
    no_dev = ''
    no_plugins = ''
    no_scripts = ''
    optimize_autoloader = ''
    prefer_dist = ''
    prefer_source = ''
    working_dir = ''
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

