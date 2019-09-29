import random
import string
import os
from register import registerObj
import writer

class ovirt_storage_domain:
    playbook_name = ''
    hosts=[]
    register=[]
    auth = ''
    backup = ''
    comment = ''
    critical_space_action_blocker = ''
    data_center = ''
    description = ''
    destroy = ''
    discard_after_delete = ''
    domain_function = ''
    fcp = ''
    fetch_nested = ''
    format = ''
    glusterfs = ''
    host = ''
    id = ''
    iscsi = ''
    localfs = ''
    name = ''
    nested_attributes = ''
    nfs = ''
    poll_interval = ''
    posixfs = ''
    state = ''
    timeout = ''
    wait = ''
    warning_low_space = ''
    wipe_after_delete = ''
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

