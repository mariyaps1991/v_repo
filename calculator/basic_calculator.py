
class BasicCalculator:

    count = 0

    def __init__(self):
        self.count += 1
        #BasicCalculator.count += 1

    @staticmethod
    def addition(priceList):
        return sum(priceList)

    @staticmethod
    def subtraction(arg1, arg2):
        return arg1 - arg2

    def multiplication(self, *args):
        result = 1
        for num in args:
            result *= num
        return result

    def obj_overwrite_count(self, value):
        self.count = value
        return self.count

    @classmethod
    def class_var_overwrite_count(cls, value):
        cls.count = value
        return cls.count


if __name__ == '__main__':
    bc1 = BasicCalculator()
    bc2 = BasicCalculator()
    print(bc1.count)
    print(bc2.count)
    """
    print("*"*50)
    bc2.count = 1
    print(bc1.count)
    print(bc2.count)
    print(BasicCalculator.count)

    print("*" * 50)
    print(bc1.obj_overwrite_count(20))
    print(bc2.count)

    print("*" * 50)
    # TO DO:: Check class level variable overwrite
    print(bc1.class_var_overwrite_count(100))
    print(bc1.count)
    print(bc2.count)

    bc3 = BasicCalculator()
    bc4 = BasicCalculator()
    print(bc3.count)
    print(bc4.count)
    """
    res = bc1.addition(10, 20, 30)
    print(res)
    res = BasicCalculator.addition(10, 20, 30, 40)
    print(res)

