
# variable length argument function

def add(*params):
    print("Parameters: ", params)
    print("Type: ", type(params))
    #(v1, v2, v3, v4) = params
    #print(f"v1: {v1}, v2:{v2}, v3:{v3}, v4:{v4}")
    return sum(params)

result = add(100, 200, 300, 400)
print(result)
print(add(100, 200))
add(100, 200, 300)