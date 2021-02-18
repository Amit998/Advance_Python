import sys
import getopt



filename="test.txt"
message="Hello"

opts,args=getopt.getopt(sys.argv[1:],"f:m:t",['filename','message'])

# print(opts)
# print(args)

# print(opts['-m'])
# print(args)


for opt,arg in opts:
    if (opt == '-f'):
        filename= arg
    if (opt == '-m'):
        filename= arg


with open(filename,'w+') as f:
    f.write(message)

# print(sys.argv)
# print(sys.argv[1])


# filename=sys.argv[1]
# message=sys.argv[2]



# with open(filename,'w+') as f:
#     f.write(message)