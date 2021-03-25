# This code is to Automate SSH to my Raspberry Pi and update it.


import paramiko
# create client ssh object so we can use it to connect to the server
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # THE MISSING KEY WILL BE ADDED

ssh.connect('10.0.0.12', username='pi', password='raspberry')

stdin, stdout, stderr = ssh.exec_command('''sudo apt-get update ''')  
stdin.flush()
data = stdout.read().splitlines()
for line in data:
    print(line)

ssh.close()
