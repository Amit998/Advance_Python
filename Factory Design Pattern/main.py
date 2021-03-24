from abc import ABCMeta,abstractstaticmethod


class IPerson(metaclass=ABCMeta):

    @abstractstaticmethod
    def person_method():
        """INTERFACE METHOD"""



class Student(IPerson):
    def __init__(self):
        self.name="Basic Student Name"
    
    def person_method(self):
        print("i am a student")

class Teacher(IPerson):
    def __init__(self):
        self.name="Basic Student Name"
    def person_method(self):
        print("Basic Teacher Name")
        

class PersonFactory:

    @staticmethod
    def build_person(person_type):
        if person_type=="Student":
            return Student()
        if person_type == "Teacher":
            return Teacher()
        print("Invalid Type")
        return -1

# p1=IPerson()
# p1.person_method()

# s1=Student()
# t1=Teacher()

# s1.person_method()
# t1.person_method()  

if __name__=="__main__":
    choice=input("What type of person do you want to create?\n")
    person=PersonFactory.build_person(choice)
    person.person_method()