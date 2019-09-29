import random
import string
import os
from register import registerObj
import writer

class user:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    append = ''
    authorization = ''
    comment = ''
    create_home = ''
    expires = ''
    force = ''
    generate_ssh_key = ''
    group = ''
    groups = ''
    hidden = ''
    home = ''
    local = ''
    login_class = ''
    move_home = ''
    non_unique = ''
    password = ''
    password_lock = ''
    profile = ''
    remove = ''
    role = ''
    seuser = ''
    shell = ''
    skeleton = ''
    ssh_key_bits = ''
    ssh_key_comment = ''
    ssh_key_file = ''
    ssh_key_passphrase = ''
    ssh_key_type = ''
    state = ''
    system = ''
    uid = ''
    update_password = ''
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

