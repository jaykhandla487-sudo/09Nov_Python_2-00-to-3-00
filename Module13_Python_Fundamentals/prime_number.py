num = int(input("Enter number: "))

flag = True

for i in range(2, num):
    if num % i == 0:
        flag = False
        break

if flag:
    print("Prime number")
else:
    print("Not prime")