import random
import string
import os
from register import registerObj
import writer

class fmgr_fwpol_package:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    object_type = ''
    adom = ''
    central_nat = ''
    fwpolicy6_implicit_log = ''
    fwpolicy_implicit_log = ''
    inspection_mode = ''
    mode = ''
    ngfw_mode = ''
    package_folder = ''
    parent_folder = ''
    scope_members = ''
    scope_members_vdom = ''
    ssl_ssh_profile = ''
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

