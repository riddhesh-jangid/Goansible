import random
import string
import os
from register import registerObj
import writer

class homebrew_cask:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    accept_external_apps = ''
    greedy = ''
    install_options = ''
    path = ''
    state = ''
    sudo_password = ''
    update_homebrew = ''
    upgrade = ''
    upgrade_all = ''
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

