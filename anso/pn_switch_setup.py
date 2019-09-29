import random
import string
import os
from register import registerObj
import writer

class pn_switch_setup:
    playbook_name = ''
    hosts=[]
    register=[]
    state = ''
    pn_analytics_store = ''
    pn_banner = ''
    pn_cliswitch = ''
    pn_date = ''
    pn_dns_ip = ''
    pn_dns_secondary_ip = ''
    pn_domain_name = ''
    pn_enable_host_ports = ''
    pn_eula_accepted = ''
    pn_eula_timestamp = ''
    pn_force = ''
    pn_gateway_ip = ''
    pn_gateway_ip6 = ''
    pn_in_band_ip = ''
    pn_in_band_ip6 = ''
    pn_in_band_ip6_assign = ''
    pn_in_band_netmask = ''
    pn_in_band_netmask_ip6 = ''
    pn_loopback_ip = ''
    pn_loopback_ip6 = ''
    pn_mgmt_ip = ''
    pn_mgmt_ip6 = ''
    pn_mgmt_ip6_assignment = ''
    pn_mgmt_ip_assignment = ''
    pn_mgmt_netmask = ''
    pn_mgmt_netmask_ip6 = ''
    pn_motd = ''
    pn_ntp_secondary_server = ''
    pn_ntp_server = ''
    pn_password = ''
    pn_switch_name = ''
    pn_timezone = ''
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

