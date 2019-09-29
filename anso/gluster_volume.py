import random
import string
import os
from register import registerObj
import writer

class gluster_volume:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    state = ''
    arbiters = ''
    bricks = ''
    cluster = ''
    directory = ''
    disperses = ''
    force = ''
    host = ''
    options = ''
    quota = ''
    rebalance = ''
    redundancies = ''
    replicas = ''
    start_on_create = ''
    stripes = ''
    transport = ''
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

