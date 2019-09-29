import random
import string
import os
from register import registerObj
import writer

class netapp_e_volume:
    playbook_name = ''
    hosts=[]
    register=[]
    api_password = ''
    api_url = ''
    api_username = ''
    name = ''
    size = ''
    state = ''
    data_assurance_enabled = ''
    metadata = ''
    read_ahead_enable = ''
    read_cache_enable = ''
    segment_size_kb = ''
    size_unit = ''
    ssd_cache_enabled = ''
    ssid = ''
    storage_pool_name = ''
    thin_provision = ''
    thin_volume_expansion_policy = ''
    thin_volume_growth_alert_threshold = ''
    thin_volume_max_repo_size = ''
    thin_volume_repo_size = ''
    validate_certs = ''
    wait_for_initialization = ''
    workload_name = ''
    write_cache_enable = ''
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

