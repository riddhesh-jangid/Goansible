import random
import string
import os
from register import registerObj
import writer

class nxos_gir:
    playbook_name = ''
    hosts=[]
    register=[]
    state = ''
    provider = ''
    system_mode_maintenance = ''
    system_mode_maintenance_dont_generate_profile = ''
    system_mode_maintenance_on_reload_reset_reason = ''
    system_mode_maintenance_shutdown = ''
    system_mode_maintenance_timeout = ''
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

