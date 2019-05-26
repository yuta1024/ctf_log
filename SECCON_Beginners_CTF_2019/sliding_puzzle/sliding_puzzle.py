from pwn import *
import subprocess
import sys

con = remote('133.242.50.201', 24912)

for i in range(1000):
    print con.recvline()
    l1 = con.recvline().split(' ')
    print l1
    l2 = con.recvline().split(' ')
    print l2
    l3 = con.recvline().split(' ')
    print l3
    print con.recvline()
    print con.recvline()
    p = [
        l1[1], l1[3], l1[5],
        l2[1], l2[3], l2[5],
        l3[1], l3[3], l3[5],
    ]
    print p
    with open('./in.txt', mode='w') as f:
        f.write(' '.join(p))
    res = subprocess.check_output("./a.out")
    con.sendline(','.join(res.strip().split(' ')))
