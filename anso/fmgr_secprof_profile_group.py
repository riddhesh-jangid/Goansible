import random
import string
import os
from register import registerObj
import writer

class fmgr_secprof_profile_group:
    playbook_name = ''
    hosts=[]
    register=[]
    adom = ''
    application_list = ''
    av_profile = ''
    dlp_sensor = ''
    dnsfilter_profile = ''
    icap_profile = ''
    ips_sensor = ''
    mms_profile = ''
    mode = ''
    name = ''
    profile_protocol_options = ''
    spamfilter_profile = ''
    ssh_filter_profile = ''
    ssl_ssh_profile = ''
    voip_profile = ''
    waf_profile = ''
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

