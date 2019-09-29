import random
import string
import os
from register import registerObj
import writer

class fmgr_secprof_ips:
    playbook_name = ''
    hosts=[]
    register=[]
    adom = ''
    block_malicious_url = ''
    comment = ''
    entries = ''
    entries_action = ''
    entries_application = ''
    entries_exempt_ip_dst_ip = ''
    entries_exempt_ip_src_ip = ''
    entries_location = ''
    entries_log = ''
    entries_log_attack_context = ''
    entries_log_packet = ''
    entries_os = ''
    entries_protocol = ''
    entries_quarantine = ''
    entries_quarantine_expiry = ''
    entries_quarantine_log = ''
    entries_rate_count = ''
    entries_rate_duration = ''
    entries_rate_mode = ''
    entries_rate_track = ''
    entries_rule = ''
    entries_severity = ''
    entries_status = ''
    extended_log = ''
    filter = ''
    filter_action = ''
    filter_application = ''
    filter_location = ''
    filter_log = ''
    filter_log_packet = ''
    filter_name = ''
    filter_os = ''
    filter_protocol = ''
    filter_quarantine = ''
    filter_quarantine_expiry = ''
    filter_quarantine_log = ''
    filter_severity = ''
    filter_status = ''
    mode = ''
    name = ''
    override = ''
    override_action = ''
    override_exempt_ip_dst_ip = ''
    override_exempt_ip_src_ip = ''
    override_log = ''
    override_log_packet = ''
    override_quarantine = ''
    override_quarantine_expiry = ''
    override_quarantine_log = ''
    override_rule_id = ''
    override_status = ''
    replacemsg_group = ''
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

