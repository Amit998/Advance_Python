import sys

def mygenerator(x):
    for x in range(x):
         yield x ** 3


values=mygenerator(800)


for x in values:
    # print(x)
    pass


print(sys.getsizeof(values))
# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))