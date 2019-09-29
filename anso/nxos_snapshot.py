import random
import string
import os
from register import registerObj
import writer

class nxos_snapshot:
    playbook_name = ''
    hosts=[]
    register=[]
    action = ''
    compare_option = ''
    comparison_results_file = ''
    description = ''
    element_key1 = ''
    element_key2 = ''
    path = ''
    provider = ''
    row_id = ''
    save_snapshot_locally = ''
    section = ''
    show_command = ''
    snapshot1 = ''
    snapshot2 = ''
    snapshot_name = ''
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

