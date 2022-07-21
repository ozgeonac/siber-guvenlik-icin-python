import subprocess
sonuc=subprocess.check_output("nmap -sS -sV 127.0.0.1",shell=True)
print sonuc
