import random
import string
import os
from register import registerObj
import writer

class xml:
    playbook_name = ''
    hosts=[]
    register=[]
    path = ''
    xmlstring = ''
    add_children = ''
    attribute = ''
    backup = ''
    content = ''
    count = ''
    input_type = ''
    insertafter = ''
    insertbefore = ''
    namespaces = ''
    pretty_print = ''
    print_match = ''
    set_children = ''
    state = ''
    strip_cdata_tags = ''
    value = ''
    xpath = ''
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

