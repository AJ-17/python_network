import subprocess
nw=subprocess.check_output(['ping' ,'-c','5','172.17.56.1'])
decoded_nw=nw.decode('ascii')
print(decoded_nw)