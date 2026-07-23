def add():
    print("enter two numbers to add.")
    print("-" * 40)
    try:
        first = int(input("enter first number: "))
        second = int(input("enter the second number: "))
        answer = first + second
        print(f"the sum of : {first} + {second} = {answer}.")
    except ValueError:
        print("enter numbers eg:1,2,3 etc..")

def subtract():
    try:
        print("enter two numbers to subtract.")
        print("-" *40)
        first = int(input("enter first number : "))
        second = int(input("enter the second number : "))
        answer = first - second
        print(f"the subtraction of : {first} - {second} = {answer} .")
    except ValueError:
        print("enter numbers eg:1,2,3 etc..")
def multiply():
    try:
        print("enter two numbers to multiply.")
        print("-" * 30)
        first = int(input("enter first number"))
        second= int(input("enter the second number: "))
        answer = first * second
        print(f"the multiplication of : {first} x {second} = {answer}")
    except ValueError:
        print("enter numbers eg:1,2,3 etc..")
def division():
    print("enter two numbers to divide.")
    print("-" *30)
    try:
        first = int(input("enter first number: "))
        second = int(input("enter the second number : "))
        if second== 0:
            print("cannot divide by zero")
        else :
            answer = first / second
            print(f"the division of : {first} / {second} = {answer}")
    except ValueError:
        print("please enter a valid number")
def exit():
    print("DONE")
while True:
    print("-" * 30)
    print("          CALCULATOR")
    print("-" * 30)
    print("1.ADDITION.")
    print("2.SUBTRACTION.")
    print("3.MULTIPLICATION.")
    print("4.DIVISION.")
    print("5.EXIT.")
    try:
        choice = int(input("enter your choice : "))
        print("-"*40)
    except ValueError:
        print("enter a valid number from (1-5)")
        break
    if choice == 1:
        add()
    elif choice == 2:
        subtract()
    elif choice == 3:
        multiply()
    elif choice == 4:
        division()
    elif choice == 5:
        exit()
        break
    else:
        print("invalid choice.")
