

# def myFunction(myparameter :int):
    # print(myparameter)
    # if (type(myparameter) != int ):
    #     pass

def myFunction(myparameter :int) -> str:
    return f"{myparameter + 10}"

def otherfunction(otherparameter: str):
    print(otherparameter)

print(myFunction(10))



#supported in 3.9
# def do(param:list[int]):
#     print(param)