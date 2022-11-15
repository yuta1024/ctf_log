from z3 import *

a = BitVec("a", 64)
b = BitVec("b", 64)
c = BitVec("c", 64)
d = BitVec("d", 64)

s = Solver()
s.add(a + b == 0x8b228bf35f6a)
s.add(c + b == 0xe78241)
s.add(d + c == 0xfa4c1a9f)
s.add(a + d == 0x8b238557f7c8)
s.add(c ^ b ^ d == 0xf9686f4d)

r = s.check()
if r == sat:
  m = s.model()
  print(m)

