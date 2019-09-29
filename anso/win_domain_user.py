import random
import string
import os
from register import registerObj
import writer

class win_domain_user:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    account_locked = ''
    attributes = ''
    city = ''
    company = ''
    country = ''
    description = ''
    domain_password = ''
    domain_server = ''
    domain_username = ''
    email = ''
    enabled = ''
    firstname = ''
    groups = ''
    groups_action = ''
    password = ''
    password_expired = ''
    password_never_expires = ''
    path = ''
    postal_code = ''
    state = ''
    state_province = ''
    street = ''
    surname = ''
    update_password = ''
    upn = ''
    user_cannot_change_password = ''
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

