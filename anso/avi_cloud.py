import random
import string
import os
from register import registerObj
import writer

class avi_cloud:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    vtype = ''
    api_context = ''
    api_version = ''
    apic_configuration = ''
    apic_mode = ''
    avi_api_patch_op = ''
    avi_api_update_method = ''
    avi_credentials = ''
    aws_configuration = ''
    azure_configuration = ''
    cloudstack_configuration = ''
    controller = ''
    custom_tags = ''
    dhcp_enabled = ''
    dns_provider_ref = ''
    docker_configuration = ''
    east_west_dns_provider_ref = ''
    east_west_ipam_provider_ref = ''
    enable_vip_static_routes = ''
    ipam_provider_ref = ''
    license_tier = ''
    license_type = ''
    linuxserver_configuration = ''
    mesos_configuration = ''
    mtu = ''
    nsx_configuration = ''
    obj_name_prefix = ''
    openstack_configuration = ''
    oshiftk8s_configuration = ''
    password = ''
    prefer_static_routes = ''
    proxy_configuration = ''
    rancher_configuration = ''
    state = ''
    state_based_dns_registration = ''
    tenant = ''
    tenant_ref = ''
    tenant_uuid = ''
    url = ''
    username = ''
    uuid = ''
    vca_configuration = ''
    vcenter_configuration = ''
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

