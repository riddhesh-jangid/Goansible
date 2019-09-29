import random
import string
import os
from register import registerObj
import writer

class fortios_ipv4_policy:
    playbook_name = ''
    hosts=[]
    register=[]
    id = ''
    application_list = ''
    av_profile = ''
    backup = ''
    backup_filename = ''
    backup_path = ''
    comment = ''
    config_file = ''
    dst_addr = ''
    dst_addr_negate = ''
    dst_intf = ''
    file_mode = ''
    fixedport = ''
    host = ''
    ips_sensor = ''
    logtraffic = ''
    logtraffic_start = ''
    nat = ''
    password = ''
    policy_action = ''
    poolname = ''
    schedule = ''
    service = ''
    service_negate = ''
    src_addr = ''
    src_addr_negate = ''
    src_intf = ''
    state = ''
    timeout = ''
    username = ''
    vdom = ''
    webfilter_profile = ''
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

