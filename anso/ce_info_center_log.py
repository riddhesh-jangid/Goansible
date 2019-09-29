import random
import string
import os
from register import registerObj
import writer

class ce_info_center_log:
    playbook_name = ''
    hosts=[]
    register=[]
    channel_id = ''
    log_buff_enable = ''
    log_buff_size = ''
    log_enable = ''
    log_level = ''
    log_time_stamp = ''
    module_name = ''
    state = ''
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

