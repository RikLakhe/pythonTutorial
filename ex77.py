import datetime
import glob

content = []

for filename in fileName:
    with open(filename,'r') as file:
        content.append(file.read())


with open(str(datetime.datetime.now())+'.txt','w') as file2:
    for cont in content:
        file2.write(cont+'\n')

