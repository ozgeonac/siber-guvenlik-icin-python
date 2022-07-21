import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy( paramiko.AutoAddPolicy())
ssh.connect('127.0.0.1', username='kali', password='kali')
stdin, stdout, stderr =  ssh.exec_command("""grep "sudo" /etc/group|cut -d ":" -f4""")
print("Sudo grubundaki kullanıcılar:")
print(stdout.read())