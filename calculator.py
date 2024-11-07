print("Welcome to Calculator Project")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

option = int(input("Select an Option For Basic Calculator Operation: "))

if option == 1:
    n1=int(input("Enter 1st Number: "))
    n2=int(input("Enter 2nd Number: "))
    sum=n1+n2
    print(f"Addition of {n1} + {n2}= {sum}")
elif option == 2:
    n1=int(input("Enter 1st Number: "))
    n2=int(input("Enter 2nd Number: "))
    sub=n1-n2
    print(f"Subtraction of {n1} - {n2}= {sub}")
elif option == 3:
    n1=int(input("Enter 1st Number: "))
    n2=int(input("Enter 2nd Number: "))
    mul=int(n1*n2)
    print(f"Multiplication of {n1} * {n2} = {mul}")
elif option == 4:
    n1=int(input("Enter 1st Number: "))
    n2=int(input("Enter 2nd Number: "))
    div=int(n1/n2)
    print(f"Division of {n1} / {n2} = {div}")
else:
    print("Invalid Input")
