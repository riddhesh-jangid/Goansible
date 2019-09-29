import random
import string
import os
from register import registerObj
import writer

class fmgr_fwobj_service:
    playbook_name = ''
    hosts=[]
    register=[]
    adom = ''
    app_category = ''
    app_service_type = ''
    application = ''
    category = ''
    check_reset_range = ''
    color = ''
    comment = ''
    custom_type = ''
    explicit_proxy = ''
    fqdn = ''
    group_member = ''
    group_name = ''
    icmp_code = ''
    icmp_type = ''
    iprange = ''
    mode = ''
    name = ''
    object_type = ''
    protocol = ''
    protocol_number = ''
    sctp_portrange = ''
    session_ttl = ''
    tcp_halfclose_timer = ''
    tcp_halfopen_timer = ''
    tcp_portrange = ''
    tcp_timewait_timer = ''
    udp_idle_timer = ''
    udp_portrange = ''
    visibility = ''
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

