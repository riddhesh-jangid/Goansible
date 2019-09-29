import random
import string
import os
from register import registerObj
import writer

class ovirt_cluster:
    playbook_name = ''
    hosts=[]
    register=[]
    auth = ''
    name = ''
    ballooning = ''
    comment = ''
    compatibility_version = ''
    cpu_arch = ''
    cpu_type = ''
    data_center = ''
    description = ''
    external_network_providers = ''
    fence_connectivity_threshold = ''
    fence_enabled = ''
    fence_skip_if_connectivity_broken = ''
    fence_skip_if_gluster_bricks_up = ''
    fence_skip_if_gluster_quorum_not_met = ''
    fence_skip_if_sd_active = ''
    fetch_nested = ''
    firewall_type = ''
    gluster = ''
    gluster_tuned_profile = ''
    ha_reservation = ''
    host_reason = ''
    id = ''
    ksm = ''
    ksm_numa = ''
    mac_pool = ''
    memory_policy = ''
    migration_auto_converge = ''
    migration_bandwidth = ''
    migration_bandwidth_limit = ''
    migration_compressed = ''
    migration_policy = ''
    nested_attributes = ''
    network = ''
    poll_interval = ''
    resilience_policy = ''
    rng_sources = ''
    scheduling_policy = ''
    scheduling_policy_properties = ''
    serial_policy = ''
    serial_policy_value = ''
    spice_proxy = ''
    state = ''
    switch_type = ''
    threads_as_cores = ''
    timeout = ''
    trusted_service = ''
    virt = ''
    vm_reason = ''
    wait = ''
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

