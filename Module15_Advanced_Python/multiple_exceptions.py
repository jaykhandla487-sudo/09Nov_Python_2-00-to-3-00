try:
    num = int(input("Enter number: "))
    result = 10 / num
    print(result)

except ValueError:
    print("Enter valid integer")

except ZeroDivisionError:
    print("Cannot divide by zero")

except Exception as e:
    print("Error:", e)