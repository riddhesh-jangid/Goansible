import random
import string
import os
from register import registerObj
import writer

class win_chocolatey:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    allow_empty_checksums = ''
    allow_multiple = ''
    allow_prerelease = ''
    architecture = ''
    force = ''
    ignore_checksums = ''
    ignore_dependencies = ''
    install_args = ''
    package_params = ''
    pinned = ''
    proxy_password = ''
    proxy_url = ''
    proxy_username = ''
    skip_scripts = ''
    source = ''
    source_password = ''
    source_username = ''
    state = ''
    timeout = ''
    validate_certs = ''
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

