import random
import string
import os
from register import registerObj
import writer

class ucs_service_profile_template:
    playbook_name = ''
    hosts=[]
    register=[]
    hostname = ''
    name = ''
    password = ''
    bios_policy = ''
    boot_policy = ''
    description = ''
    graphics_card_policy = ''
    host_firmware_package = ''
    ipmi_access_profile = ''
    iqn_pool = ''
    kvm_mgmt_policy = ''
    lan_connectivity_policy = ''
    local_disk_policy = ''
    maintenance_policy = ''
    mgmt_inband_pool_name = ''
    mgmt_interface_mode = ''
    mgmt_ip_pool = ''
    mgmt_vnet_name = ''
    org_dn = ''
    port = ''
    power_control_policy = ''
    power_state = ''
    power_sync_policy = ''
    proxy = ''
    san_connectivity_policy = ''
    scrub_policy = ''
    server_pool = ''
    server_pool_qualification = ''
    sol_policy = ''
    state = ''
    storage_profile = ''
    template_type = ''
    threshold_policy = ''
    use_proxy = ''
    use_ssl = ''
    user_label = ''
    username = ''
    uuid_pool = ''
    vmedia_policy = ''
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

