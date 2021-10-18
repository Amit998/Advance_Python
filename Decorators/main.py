import functools




# @mydecorator
# def desomthing():
#     pass


# def start_end_decorator(func):

#     @functools.wraps(func)
#     def wrapper(*args,**kwargs):
#         print("start")
#         result=func(*args,**kwargs)
#         print("End")
#         return result

#     return wrapper


# @start_end_decorator
# def print_name():
#     print("alex")

# @start_end_decorator
# def add5(x):
#     return x+5


# print_name=start_end_decorator(print_name)

# print_name()

# print(add5.__name__)




# def repeater(num_times):

#     def decorator_repeat(func):
        
#         @functools.wraps(func)
#         def wrapper(*args,**kwargs):
#             for _ in range(num_times):
#                 result=func(*args,**kwargs)

#             return result
#         return wrapper
#     return decorator_repeat


# @repeater(num_times=5)
# def greet(name):
#     print(f'Hello {name}')

# greet("Amit")

# def debug(func):
#     @functools.wraps
#     def wrapper(*args,**kwargs):
#         args_repr=[repr(a) for a in args]
#         kwargs_repr=[f"{k} ={v!r}" for k,v in kwargs.items()]
#         signature=", ".join(args_repr + kwargs_repr)
#         print(f"Calling {func.__name__} ({signature})")
#         result=func(*args,**kwargs)
#         print(f" {func.__name__!r} returned ({result!r})")

#         return result
#     return wrapper



# def start_end_decorator(func):

#     @functools.wraps(func)
#     def wrapper(*args,**kwargs):
#         print("start")
#         result=func(*args,**kwargs)
#         print("End")
#         return result

#     return wrapper

# @debug
# @start_end_decorator
# def say_hello(name):
#     greeting= f"Hello {name}"
#     print(name)
#     return greeting

# say_hello("Alex")


class CountCalls:
    def __init__(self,func):
        self.func=func
        self.num_calls=0
    
    def __call__(self,*agrs,**kwargs):
        print("Hi There")
        self.num_calls+=1

        print(f"This is executed {self.num_calls} times")
        return self.func(*agrs,**kwargs)

# cc=CountCalls(None)
# cc()

@CountCalls
def say_hello():
    print("Hello")

say_hello()
say_hello()