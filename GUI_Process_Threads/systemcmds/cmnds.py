

if False:
    import os 
# os.system("ls -l ")#first way
'''second way '''
if False:
    import os 
    output =os.popen("ls -l ")
    print(output.read())
''' third way '''
import subprocess
output=subprocess.Popen(["ls","-l"])
