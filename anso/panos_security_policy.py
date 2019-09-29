import random
import string
import os
from register import registerObj
import writer

class panos_security_policy:
    playbook_name = ''
    hosts=[]
    register=[]
    ip_address = ''
    password = ''
    rule_name = ''
    action = ''
    antivirus = ''
    api_key = ''
    application = ''
    commit = ''
    data_filtering = ''
    description = ''
    destination = ''
    devicegroup = ''
    file_blocking = ''
    from_zone = ''
    group_profile = ''
    hip_profiles = ''
    log_end = ''
    log_start = ''
    rule_type = ''
    service = ''
    source = ''
    source_user = ''
    spyware = ''
    tag = ''
    to_zone = ''
    url_filtering = ''
    username = ''
    vulnerability = ''
    wildfire_analysis = ''
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

