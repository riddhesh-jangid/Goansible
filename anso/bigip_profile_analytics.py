import random
import string
import os
from register import registerObj
import writer

class bigip_profile_analytics:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    password = ''
    server = ''
    user = ''
    collect_geo = ''
    collect_ip = ''
    collect_max_tps_and_throughput = ''
    collect_page_load_time = ''
    collect_url = ''
    collect_user_agent = ''
    collect_user_sessions = ''
    collected_stats_external_logging = ''
    collected_stats_internal_logging = ''
    description = ''
    external_logging_publisher = ''
    notification_by_email = ''
    notification_by_syslog = ''
    notification_email_addresses = ''
    parent = ''
    partition = ''
    provider = ''
    server_port = ''
    state = ''
    validate_certs = ''
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

