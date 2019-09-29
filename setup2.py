import os
import subprocess as sb
import re
counter=1

os.system('mkdir anso')
with open('dictionary','r') as Pdictionary:
    for module in Pdictionary:
        class_name = re.sub('\n','',module)
        class_path = "./anso/"+class_name+".py"
        pointer = open(class_path,'w')
        compath = "./compulsery/"+class_name
        othpath = "./others/"+class_name
        pointer.write('import random\n')
        pointer.write('import string\n')
        pointer.write('import os\n')
        pointer.write('from register import registerObj\n')
        pointer.write('import writer\n\n')
        pointer.write('class {}:\n'.format(class_name))
        pointer.write('    playbook_name = \'\'\n')
        pointer.write('    hosts=[]\n')
        pointer.write('    register=[]\n')
        with open(compath,'r') as Pcompulsery:
            for attr in Pcompulsery:
                attr = re.sub('\n','',attr)
                pointer.write("    {} = \'\'\n".format(attr))
        with open(othpath,'r') as Pothers:
            for attr in Pothers:
                attr = re.sub('\n','',attr)
                pointer.write("    {} = \'\'\n".format(attr))
        
        pointer.write("    def compile(self):\n") 
        pointer.write("       self.playbook_name=writer.writer(self,self.playbook_name)\n\n")
        pointer.write("    def run(self):\n")
        pointer.write("       dump_name=''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])\n")
        pointer.write("       os.system('{} | tee {}'.format(self.playbook_name,dump_name))\n")
        pointer.write("       self.register = registerObj(dump_name)\n")
        pointer.write("       os.remove(dump_name)\n\n")
        pointer.write("    def go(self):\n")
        pointer.write("       self.compile()\n")
        pointer.write("       self.run()\n\n")
        pointer.close()
        print("Process :: {}/2843".format(counter),end='\r')
        counter+=1
