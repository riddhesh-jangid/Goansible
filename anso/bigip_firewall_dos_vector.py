import random
import string
import os
from register import registerObj
import writer

class bigip_firewall_dos_vector:
    playbook_name = ''
    hosts=[]
    register=[]
    password = ''
    profile = ''
    server = ''
    state = ''
    user = ''
    allow_advertisement = ''
    attack_ceiling = ''
    attack_floor = ''
    auto_blacklist = ''
    bad_actor_detection = ''
    blacklist_detection_seconds = ''
    blacklist_duration = ''
    detection_threshold_eps = ''
    detection_threshold_percent = ''
    mitigation_threshold_eps = ''
    name = ''
    partition = ''
    per_source_ip_detection_threshold = ''
    per_source_ip_mitigation_threshold = ''
    provider = ''
    server_port = ''
    simulate_auto_threshold = ''
    threshold_mode = ''
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

