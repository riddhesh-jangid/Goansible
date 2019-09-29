import random
import string
import os
from register import registerObj
import writer

class portage:
    playbook_name = ''
    hosts=[]
    register=[]
    changed_use = ''
    deep = ''
    depclean = ''
    getbinpkg = ''
    jobs = ''
    keepgoing = ''
    loadavg = ''
    newuse = ''
    nodeps = ''
    noreplace = ''
    oneshot = ''
    onlydeps = ''
    package = ''
    quiet = ''
    quietbuild = ''
    quietfail = ''
    state = ''
    sync = ''
    update = ''
    usepkgonly = ''
    verbose = ''
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

