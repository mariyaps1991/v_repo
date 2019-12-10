

class School:
    print("From school class")      #--> data member
    name = "Navodhaya"
    __School_code = "N001"          # private
    __place = "Chennai"             # private

    def __init__(self):
        self.a = 100

    def teach(self):
        #print(dir(self))
        subject = "Science"
        print("We teach science")

    def __practice_yoga(self):      # private
        print("Training is started.")

    def get_school_code(self):
        return School.__School_code

    def __del__(self):
        print("Destroyed all objects and variables")


if __name__ == '__main__':
    """
    obj1 = School()
    obj2 = School()
    print(obj1.name)
    print(obj2.name)
    #print(obj1.__School_code)
    #print(obj1.__place)
    print(obj1.get_school_code())
    print(obj1._School__School_code)
    print(obj1._School__practice_yoga())
    obj1.name = "Government school"
    print(obj1.name)
    print(dir(obj1))
    #print(help(obj1))
    print(obj1.teach())
    #print(dir(obj1))
    """
    School().teach()
    #School.teach(School)
    print(School().a)


    s1 = School()
    s1.teach()
    print("Call-1: ", s1.a)
    print("Call-2: ", s1.a)



