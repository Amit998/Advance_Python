class Person:

    def __init__(self,name,age,gender):
        self.__name=name
        self.__age=age
        self.__gender=gender

    @property
    def Name(self):
        return self.__name
    
    @Name.setter
    def Name(self,value):
        if value == "BOB":
            self.__name="Default Name"
        else:
            self.__name=value
    
    @staticmethod
    def myMethod():
        print("Hello World")


Person.myMethod()

# p1=Person("Mike",20,"m")
# print(p1.Name)

# p1.myMethod()
# p1.Name="BOB"

# print(p1.Name)