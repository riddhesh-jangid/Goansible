import random
import string
import os
from register import registerObj
import writer

class fmgr_secprof_dns:
    playbook_name = ''
    hosts=[]
    register=[]
    adom = ''
    block_action = ''
    block_botnet = ''
    comment = ''
    domain_filter_domain_filter_table = ''
    external_ip_blocklist = ''
    ftgd_dns_filters_action = ''
    ftgd_dns_filters_category = ''
    ftgd_dns_filters_log = ''
    ftgd_dns_options = ''
    log_all_domain = ''
    mode = ''
    name = ''
    redirect_portal = ''
    safe_search = ''
    sdns_domain_log = ''
    sdns_ftgd_err_log = ''
    youtube_restrict = ''
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

