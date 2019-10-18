
# keyword variable length argument function

def add(**args):
    print("Args: ", args)
    print("Type:", type(args))
    return sum(args.values())

print(add(arg2=10, arg1=100))
print(add(arg1=100, arg2=300, arg3=300))