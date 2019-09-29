import random
import string
import os
from register import registerObj
import writer

class meraki_ssid:
    playbook_name = ''
    hosts=[]
    register=[]
    ap_tags_vlan_ids = ''
    auth_key = ''
    auth_mode = ''
    band_selection = ''
    concentrator_network_id = ''
    default_vlan_id = ''
    enabled = ''
    encryption_mode = ''
    host = ''
    ip_assignment_mode = ''
    min_bitrate = ''
    name = ''
    net_id = ''
    net_name = ''
    number = ''
    org_id = ''
    org_name = ''
    output_level = ''
    per_client_bandwidth_limit_down = ''
    per_client_bandwidth_limit_up = ''
    psk = ''
    radius_accounting_enabled = ''
    radius_accounting_servers = ''
    radius_coa_enabled = ''
    radius_failover_policy = ''
    radius_load_balancing_policy = ''
    radius_servers = ''
    splash_page = ''
    state = ''
    timeout = ''
    use_https = ''
    use_proxy = ''
    use_vlan_tagging = ''
    validate_certs = ''
    vlan_id = ''
    walled_garden_enabled = ''
    walled_garden_ranges = ''
    wpa_encryption_mode = ''
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

