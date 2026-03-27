def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

print("1.Add 2.Subtract 3.Multiply 4.Divide")

choice = int(input("Choose operation: "))

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if choice == 1:
    print(add(a,b))
elif choice == 2:
    print(sub(a,b))
elif choice == 3:
    print(mul(a,b))
elif choice == 4:
    print(div(a,b))
else:
    print("Invalid choice")