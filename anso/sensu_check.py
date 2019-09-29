import random
import string
import os
from register import registerObj
import writer

class sensu_check:
    playbook_name = ''
    hosts=[]
    register=[]
    command = ''
    name = ''
    aggregate = ''
    backup = ''
    custom = ''
    dependencies = ''
    handle = ''
    handlers = ''
    high_flap_threshold = ''
    interval = ''
    low_flap_threshold = ''
    metric = ''
    occurrences = ''
    path = ''
    publish = ''
    refresh = ''
    source = ''
    standalone = ''
    state = ''
    subdue_begin = ''
    subdue_end = ''
    subscribers = ''
    timeout = ''
    ttl = ''
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

