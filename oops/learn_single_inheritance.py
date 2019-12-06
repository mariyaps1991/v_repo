

class BaseClass:

    def __init__(self, name):
        print("object for this class is created.")
        self.name = name

    def get_age(self, age):
        print("Age information from BaseClass")
        return age + 2

    def get_name(self):
        return self.name


class DerivedClass(BaseClass):

    def get_age(self, age):
        bc = BaseClass(self.name)
        age = bc.get_age(age)
        return age


myname = "Vasanth"
person1 = DerivedClass(myname)
#print(dir(bc))
print(person1.name)

print(person1.get_name())
print(person1.get_age(26))
