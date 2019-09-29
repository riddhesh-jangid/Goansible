import random
import string
import os
from register import registerObj
import writer

class fmgr_secprof_appctrl:
    playbook_name = ''
    hosts=[]
    register=[]
    adom = ''
    app_replacemsg = ''
    comment = ''
    deep_app_inspection = ''
    entries = ''
    entries_action = ''
    entries_application = ''
    entries_behavior = ''
    entries_category = ''
    entries_log = ''
    entries_log_packet = ''
    entries_parameters_value = ''
    entries_per_ip_shaper = ''
    entries_popularity = ''
    entries_protocols = ''
    entries_quarantine = ''
    entries_quarantine_expiry = ''
    entries_quarantine_log = ''
    entries_rate_count = ''
    entries_rate_duration = ''
    entries_rate_mode = ''
    entries_rate_track = ''
    entries_risk = ''
    entries_session_ttl = ''
    entries_shaper = ''
    entries_shaper_reverse = ''
    entries_sub_category = ''
    entries_technology = ''
    entries_vendor = ''
    extended_log = ''
    mode = ''
    name = ''
    options = ''
    other_application_action = ''
    other_application_log = ''
    p2p_black_list = ''
    replacemsg_group = ''
    unknown_application_action = ''
    unknown_application_log = ''
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

