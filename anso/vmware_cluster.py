import random
import string
import os
from register import registerObj
import writer

class vmware_cluster:
    playbook_name = ''
    hosts=[]
    register=[]
    cluster_name = ''
    datacenter = ''
    drs_default_vm_behavior = ''
    drs_enable_vm_behavior_overrides = ''
    drs_vmotion_rate = ''
    enable_drs = ''
    enable_ha = ''
    enable_vsan = ''
    ha_admission_control_enabled = ''
    ha_failover_level = ''
    ha_host_monitoring = ''
    ha_restart_priority = ''
    ha_vm_failure_interval = ''
    ha_vm_max_failure_window = ''
    ha_vm_max_failures = ''
    ha_vm_min_up_time = ''
    ha_vm_monitoring = ''
    hostname = ''
    password = ''
    port = ''
    state = ''
    username = ''
    validate_certs = ''
    vsan_auto_claim_storage = ''
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

