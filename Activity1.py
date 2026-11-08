def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b
fun = input("Enter the function you want to use(add, subtract, multiply, divide): ").lower().strip()
num = float(input("Enter a number: "))
num_2 = float(input("Enter another number: "))

try:
    if fun == "add":
        result = add(num, num_2)
        print("Your result is ", result)
    elif fun == "subtract":
        result = subtract(num, num_2)
        print("Your result is ", result)
    elif fun == "multipy":
        result = multiply(num, num_2)
        print("Your result is ", result)
    elif fun == "divide":
        result = divide(num, num_2)
        print("Your result is ", result)
    else:
        print("Write the correct spelling.")
except ValueError:
    print("Write can only number")
except ZeroDivisionError:
    print("you can not enter 0")
