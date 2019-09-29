import random
import string
import os
from register import registerObj
import writer

class maven_artifact:
    playbook_name = ''
    hosts=[]
    register=[]
    artifact_id = ''
    dest = ''
    group_id = ''
    attributes = ''
    classifier = ''
    extension = ''
    group = ''
    headers = ''
    keep_name = ''
    mode = ''
    owner = ''
    password = ''
    repository_url = ''
    selevel = ''
    serole = ''
    setype = ''
    seuser = ''
    state = ''
    timeout = ''
    unsafe_writes = ''
    username = ''
    validate_certs = ''
    verify_checksum = ''
    version = ''
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

