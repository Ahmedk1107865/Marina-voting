import os,sys,platform
bit = platform.architecture()[0]
if bit == '64bit':
    os.system('chmod +x sarkar')
    os.system('./marina')
elif bit == '32bit':
    os.system('chmod +x sarkar32')
    os.system('./marina32')
else:
    print('device not supported')
