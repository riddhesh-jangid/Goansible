import random
import string
import os
from register import registerObj
import writer

class cs_snapshot_policy:
    playbook_name = ''
    hosts=[]
    register=[]
    account = ''
    api_http_method = ''
    api_key = ''
    api_region = ''
    api_secret = ''
    api_timeout = ''
    api_url = ''
    device_id = ''
    domain = ''
    interval_type = ''
    max_snaps = ''
    project = ''
    schedule = ''
    state = ''
    time_zone = ''
    vm = ''
    volume = ''
    volume_type = ''
    vpc = ''
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

