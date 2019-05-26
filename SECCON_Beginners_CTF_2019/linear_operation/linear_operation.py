import angr

p = angr.Project('./linear_operation', load_options={'auto_load_libs': False})

addr_main = 0x40cee1
addr_succeeded = 0x40cf78 
addr_failed = 0x40cf86
print "main = %x" % addr_main
print "succeeded = %x" % addr_succeeded
print "failed = %x" % addr_failed

initial_state = p.factory.blank_state(addr=addr_main)
initial_path = p.factory.path(initial_state)
pg = p.factory.path_group(initial_path)
e = pg.explore(find=(addr_succeeded,), avoid=(addr_failed,))

if len(e.found) > 0:
    print 'Dump stdin at succeeded():'
    s = e.found[0].state
    print "%r" % s.posix.dumps(0)
