import random
import string
import os
from register import registerObj
import writer

class pn_connection_stats_settings:
    playbook_name = ''
    hosts=[]
    register=[]
    state = ''
    pn_client_server_stats_log_disk_space = ''
    pn_client_server_stats_log_enable = ''
    pn_client_server_stats_log_interval = ''
    pn_client_server_stats_max_memory = ''
    pn_cliswitch = ''
    pn_connection_backup_enable = ''
    pn_connection_backup_interval = ''
    pn_connection_max_memory = ''
    pn_connection_stats_log_disk_space = ''
    pn_connection_stats_log_enable = ''
    pn_connection_stats_log_interval = ''
    pn_connection_stats_max_memory = ''
    pn_enable = ''
    pn_fabric_connection_backup_enable = ''
    pn_fabric_connection_backup_interval = ''
    pn_fabric_connection_max_memory = ''
    pn_service_stat_max_memory = ''
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

