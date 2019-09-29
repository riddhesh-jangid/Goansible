import random
import string
import os
from register import registerObj
import writer

class tower_notification:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    notification_type = ''
    account_sid = ''
    account_token = ''
    api_url = ''
    channels = ''
    client_name = ''
    color = ''
    description = ''
    from_number = ''
    headers = ''
    host = ''
    message_from = ''
    nickname = ''
    notification_configuration = ''
    notify = ''
    organization = ''
    password = ''
    port = ''
    recipients = ''
    rooms = ''
    sender = ''
    server = ''
    service_key = ''
    state = ''
    subdomain = ''
    targets = ''
    to_numbers = ''
    token = ''
    tower_config_file = ''
    tower_host = ''
    tower_password = ''
    tower_username = ''
    url = ''
    use_ssl = ''
    use_tls = ''
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

