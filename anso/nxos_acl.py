import random
import string
import os
from register import registerObj
import writer

class nxos_acl:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    ack = ''
    action = ''
    dest = ''
    dest_port1 = ''
    dest_port2 = ''
    dest_port_op = ''
    dscp = ''
    established = ''
    fin = ''
    fragments = ''
    log = ''
    precedence = ''
    proto = ''
    provider = ''
    psh = ''
    remark = ''
    rst = ''
    seq = ''
    src = ''
    src_port1 = ''
    src_port2 = ''
    src_port_op = ''
    state = ''
    syn = ''
    time_range = ''
    urg = ''
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

