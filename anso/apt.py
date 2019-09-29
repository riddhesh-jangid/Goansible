import random
import string
import os
from register import registerObj
import writer

class apt:
    playbook_name = ''
    hosts=[]
    register=[]
    allow_unauthenticated = ''
    autoclean = ''
    autoremove = ''
    cache_valid_time = ''
    deb = ''
    default_release = ''
    dpkg_options = ''
    force = ''
    force_apt_get = ''
    install_recommends = ''
    name = ''
    only_upgrade = ''
    policy_rc_d = ''
    purge = ''
    state = ''
    update_cache = ''
    upgrade = ''
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

