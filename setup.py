import os
import subprocess as sb
import re
counter = 1

docVar = sb.getoutput('ansible-doc -l')
pointer = open('dumpdict','w')
pointer.write(docVar)
pointer.close()

os.system('mkdir compulsery')
os.system('mkdir others')

pointer = open('dictionary','w')
with open('dumpdict','r') as Pdictionary:
    for module in Pdictionary:
        module = re.split('\s',module)[0]
        pointer.write(module)
        pointer.write('\n')
        compulsery_path = "./compulsery/"+module
        others_path = "./others/"+module
        
        Pdumpattr = open('dumpattr','w')
        attVar = sb.getoutput('ansible-doc {}'.format(module))
        Pdumpattr.write(attVar)
        Pdumpattr.close()
        
        Pcompulsery = open(compulsery_path,'w')
        Pothers = open(others_path,'w')
        
        with open('dumpattr','r') as Preadattr:
            for line in Preadattr:
                if len(re.findall('^EXAMPLES:',line))!=0:
                    break
                if len(re.findall('^= ',line))>0:
                    line = re.sub('= ','',line)
                    line = re.sub('\n','',line)
                    Pcompulsery.write(line)
                    Pcompulsery.write('\n')
                if len(re.findall('^- ',line))>0:
                    line = re.sub('- ','',line)
                    line = re.sub('\n','',line)
                    Pothers.write(line)
                    Pothers.write('\n')
        Pcompulsery.close()
        Pothers.close()
        
        print("Process :: {}/2834".format(counter),end='\r')
        counter+=1

pointer.close()   
os.remove('dumpdict')
os.remove('dumpattr')

