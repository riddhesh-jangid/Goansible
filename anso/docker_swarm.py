import random
import string
import os
from register import registerObj
import writer

class docker_swarm:
    playbook_name = ''
    hosts=[]
    register=[]
    state = ''
    advertise_addr = ''
    api_version = ''
    autolock_managers = ''
    ca_cert = ''
    ca_force_rotate = ''
    client_cert = ''
    client_key = ''
    debug = ''
    default_addr_pool = ''
    dispatcher_heartbeat_period = ''
    docker_host = ''
    election_tick = ''
    force = ''
    heartbeat_tick = ''
    join_token = ''
    keep_old_snapshots = ''
    labels = ''
    listen_addr = ''
    log_entries_for_slow_followers = ''
    name = ''
    node_cert_expiry = ''
    node_id = ''
    remote_addrs = ''
    rotate_manager_token = ''
    rotate_worker_token = ''
    signing_ca_cert = ''
    signing_ca_key = ''
    snapshot_interval = ''
    ssl_version = ''
    subnet_size = ''
    task_history_retention_limit = ''
    timeout = ''
    tls = ''
    tls_hostname = ''
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

