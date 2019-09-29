import random
import string
import os
from register import registerObj
import writer

class netconf_config:
    playbook_name = ''
    hosts=[]
    register=[]
    host = ''
    backup = ''
    backup_options = ''
    commit = ''
    confirm = ''
    confirm_commit = ''
    content = ''
    default_operation = ''
    delete = ''
    error_option = ''
    format = ''
    hostkey_verify = ''
    lock = ''
    look_for_keys = ''
    password = ''
    port = ''
    save = ''
    source_datastore = ''
    src = ''
    ssh_keyfile = ''
    target = ''
    timeout = ''
    username = ''
    validate = ''
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

