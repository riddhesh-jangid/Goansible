import random
import string
import os
from register import registerObj
import writer

class aci_interface_policy_leaf_policy_group:
    playbook_name = ''
    hosts=[]
    register=[]
    host = ''
    lag_type = ''
    password = ''
    private_key = ''
    aep = ''
    cdp_policy = ''
    certificate_name = ''
    description = ''
    egress_data_plane_policing_policy = ''
    fibre_channel_interface_policy = ''
    ingress_data_plane_policing_policy = ''
    l2_interface_policy = ''
    link_level_policy = ''
    lldp_policy = ''
    mcp_policy = ''
    monitoring_policy = ''
    output_level = ''
    policy_group = ''
    port = ''
    port_channel_policy = ''
    port_security_policy = ''
    priority_flow_control_policy = ''
    slow_drain_policy = ''
    state = ''
    storm_control_interface_policy = ''
    stp_interface_policy = ''
    timeout = ''
    use_proxy = ''
    use_ssl = ''
    username = ''
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

