

def myFunction(*args,**kwargs):
    print(args[0])
    print(args[1])
    print(args[2])
    print(args[3])
    print(kwargs['KEYONE'])
    print(kwargs['KEYTWO'])

myFunction('hey',True,19,'wow',KEYONE='TEST',KEYTWO=7)