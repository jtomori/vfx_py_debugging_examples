import ptvsd

# allow other computers to attach to ptvsd at this IP address and port, using the password
try:
    ptvsd.enable_attach("SFds_KjLDFJ:LK", address = ('localhost', 3000))
    print "Not attached already, attaching..."
except ptvsd.AttachAlreadyEnabledError:
    print "Attached already, continuing..."


def test():
    # pause the program until a remote debugger is attached
    ptvsd.wait_for_attach()

    # break at this line
    ptvsd.break_into_debugger()
    
    before = "before"
    after = "after"

    print before
    print after