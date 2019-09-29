import random
import string
import os
from register import registerObj
import writer

class cyberark_user:
    playbook_name = ''
    hosts=[]
    register=[]
    cyberark_session = ''
    username = ''
    change_password_on_the_next_logon = ''
    disabled = ''
    email = ''
    expiry_date = ''
    first_name = ''
    group_name = ''
    initial_password = ''
    last_name = ''
    location = ''
    new_password = ''
    state = ''
    user_type_name = ''
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

