import angr
import claripy

proj = angr.Project('./leakage', load_options={"auto_load_libs": False})

input_size = 0x22 # 4005ff
argv1 = claripy.BVS("argv1", input_size * 8)

initial_state = proj.factory.entry_state(args=["./leakage", argv1], add_options={angr.options.LAZY_SOLVES})
initial_state.libc.buf_symbolic_bytes=input_size + 1

for byte in argv1.chop(8):
  initial_state.add_constraints(byte != '\x00') # null
  initial_state.add_constraints(byte >= ' ') # '\x20'
  initial_state.add_constraints(byte <= '~') # '\x7e'

sm = proj.factory.simgr(initial_state)
sm.explore(find=0x4006ae, avoid=0x4006bc)
found = sm.found[0]
solution = found.se.eval(argv1, cast_to=str)
solution = solution[:solution.find("}")+1]
print solution
