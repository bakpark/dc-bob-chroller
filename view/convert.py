from os import listdir
import subprocess


path = '.\\publish'
for file in listdir(path):
    split = file.split('.')
    length = len(split)
    if 'ui' == split[length-1]:
        subprocess.Popen(['pyuic5','-x',path+'\\'+str(file),'-o',split[0]+'.py'],
                         stdout=subprocess.PIPE,
                         universal_newlines=True)
    print(file)

