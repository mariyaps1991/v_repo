
"""
mylist = range(0, 10, 2)
a = 100

for number in [10, 20, 30, 40]:
    print(number)
    print(a + number)

for char in "Hello World":
    print(char)

a = 1013423

for num in str(a):
    print(num)

b = list(enumerate(str(a), 11))     # pickling - bind the data/string to object
print(b)

print(b[0])
print(b[0][0])
print(b[0][1])

(name, age) = ["Mari", 28]      # unpacking
print("Name:", name)
print("Age:", age)

print("Name:", name, "Age:", age)

res_format = "Name: {} Age: {}"     # placeholders

print(res_format.format(name, age))

count = 0
max_attempt = 3

while count < max_attempt:
    count = count + 1
    if count == max_attempt:
        print("Max attempt is reached")
        #break
    else:
        print("Pls retry")

print("End")


numbers = list(range(10, 100, 5))

for number in numbers:
    if number == 50:
        break
    if number == 30:
        continue
    print("Number: ", number)


# tuple
mytuple = (10, 20, 10, 20.0)



discount = 20/100                   # global reference

def total(v1, v2, v3):
    discount = 0                    # local reference
    amount = v1 + v2 + v3
    if amount > 500:
        discount = 10/100
    net_amount = (amount * discount) + amount
    return amount, discount, net_amount


def calculate_gst(v1):
    gst = 18/100
    gst_on_amount = v1 * gst
    global discount
    print("Discount inside a function: ", discount)
    discount = discount + 5/100
    return gst_on_amount


result = total(100, 200, 300)
print(result)
amt = result[0]
dscnt = result[1]
gst_amount = result[2]
gst_amount = calculate_gst(amt)
print("Amount: ", amt)
print("Discount: ", dscnt)
print("GST on amount is ", gst_amount)

print("Discount: ", discount)
"""


from myfile import a
print(a)

