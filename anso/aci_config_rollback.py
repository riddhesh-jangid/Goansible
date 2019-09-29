import random
import string
import os
from register import registerObj
import writer

class aci_config_rollback:
    playbook_name = ''
    hosts=[]
    register=[]
    export_policy = ''
    host = ''
    password = ''
    private_key = ''
    snapshot = ''
    certificate_name = ''
    compare_export_policy = ''
    compare_snapshot = ''
    description = ''
    fail_on_decrypt = ''
    import_mode = ''
    import_policy = ''
    import_type = ''
    output_level = ''
    port = ''
    state = ''
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

