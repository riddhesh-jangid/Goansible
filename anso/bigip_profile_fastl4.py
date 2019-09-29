import random
import string
import os
from register import registerObj
import writer

class bigip_profile_fastl4:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    password = ''
    server = ''
    user = ''
    client_timeout = ''
    description = ''
    explicit_flow_migration = ''
    idle_timeout = ''
    ip_df_mode = ''
    ip_tos_to_client = ''
    ip_tos_to_server = ''
    ip_ttl_mode = ''
    ip_ttl_v4 = ''
    ip_ttl_v6 = ''
    keep_alive_interval = ''
    late_binding = ''
    link_qos_to_client = ''
    link_qos_to_server = ''
    loose_close = ''
    loose_initialization = ''
    mss_override = ''
    parent = ''
    partition = ''
    provider = ''
    reassemble_fragments = ''
    receive_window_size = ''
    reset_on_timeout = ''
    rtt_from_client = ''
    rtt_from_server = ''
    server_port = ''
    server_sack = ''
    server_timestamp = ''
    state = ''
    syn_cookie_mss = ''
    tcp_close_timeout = ''
    tcp_generate_isn = ''
    tcp_handshake_timeout = ''
    tcp_strip_sack = ''
    tcp_time_wait_timeout = ''
    tcp_timestamp_mode = ''
    tcp_wscale_mode = ''
    timeout_recovery = ''
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

