import angr
import claripy

proj = angr.Project('./chall.baby', main_opts={'base_addr': 0}, auto_load_libs=False)
arg = claripy.BVS('arg', 8*0x30)

state = proj.factory.entry_state(args=['../chall.baby', arg])
simgr = proj.factory.simulation_manager(state)
simgr.explore(find=0x12cc, avoid=[0x127d])

if len(simgr.found) > 0:
    s = simgr.found[0]
    print(s.solver.eval(arg, cast_to=bytes))
