from pwn import *
from sympy import *

x = Symbol('x')

con = remote('zerois-o-reiwa.seccon.jp', 23615)

for i in range(100):
    con.recvline()
    expr = con.recvline().replace("?", "x")
    print(i, expr)
    tmp = solve(Eq(eval(expr[2:-1]),0))
    if len(tmp) == 0:
        ans = 0
    else:
        ans = tmp[0]
    con.sendline(str(ans))

print con.recvline()
print con.recvline()
print con.recvline()
print con.recvline()
print con.recvline()
print con.recvline()
