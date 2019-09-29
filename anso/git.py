import random
import string
import os
from register import registerObj
import writer

class git:
    playbook_name = ''
    hosts=[]
    register=[]
    dest = ''
    repo = ''
    accept_hostkey = ''
    archive = ''
    bare = ''
    clone = ''
    depth = ''
    executable = ''
    force = ''
    key_file = ''
    recursive = ''
    reference = ''
    refspec = ''
    remote = ''
    separate_git_dir = ''
    ssh_opts = ''
    track_submodules = ''
    umask = ''
    update = ''
    verify_commit = ''
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

