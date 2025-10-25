import os
print(dir(os))
from datetime import datetime
print (os.getcwd())
os.chdir('/home/user/Documents')
print (os.getcwd())
print (os.listdir('/home/user'))
print (os.name)
os.mkdir('New_Folder')
os.rename('New_Folder', 'Renamed_Folder')   
os.rmdir('Renamed_Folder')
print (os.path.join('/home/user', 'Documents'))         
os.remove('/home/user/Documents/old_file.txt')
print (os.path.exists('/home/user/Documents'))
print(os.stats('/home/user/Documents').st_size)
mod_time = os.path.getmtime('/home/user/Documents')
print (mod_time)
os.walk('/home/user')
for dirpath, dirnames, filenames in os.walk('/home/user'):
    print('Current Path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)

#print(os.environ.get('HOME'))
file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
print(file_path)

with open(file_path, 'w') as f:
    f.write('Hello, World!')

os.path.basename('/home/user/Documents/test.txt')
os.path.exists('/home/user/Documents/test.txt')
mod_time = os.path.isdir('/home/user/Documents')
os.path.isfile('/home/user/Documents/test.txt')
os.path.splitext('/home/user/Documents/test.txt')
print(datetime.fromtimestamp(mod_time))
print (os.path.abspath('test.txt')) 
print (os.path.dirname('/home/user/Documents/test.txt'))
print(dir(os.path))