import random
import string
import os
from register import registerObj
import writer

class gem:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    build_flags = ''
    env_shebang = ''
    executable = ''
    force = ''
    gem_source = ''
    include_dependencies = ''
    include_doc = ''
    install_dir = ''
    pre_release = ''
    repository = ''
    state = ''
    user_install = ''
    version = ''
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

