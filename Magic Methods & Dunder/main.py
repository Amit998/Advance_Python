# class Person:

#     def __init__(self,name,age):
#         self.name = name
#         self.age=age
    
    
#     def __del__(self):
#         print("Object is distructed")


# p=Person('Amit',12)


class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        return Vector(self.x + other.x ,self.y +other.y)
    def __sub__(self,other):
        return Vector(self.x - other.x ,self.y - other.y)
    def __repr__(self):
        return f"X: {self.x} ,Y: {self.y} "
    
    def __len__(self):
        return 10
    
    def __call__(self):
        print("Hello ! I Was Called!")


v1=Vector(10,20)
v2=Vector(11,22)
v3= v1 + v2

print(len(v3))

v3()

v1()