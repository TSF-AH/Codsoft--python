from random import choice
try:
    password = []
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
    user = int(input("Enter the length for your passsword : "))
    if user > 30 :
        print("very lengthy password .. best between(10-30)")
    elif user < 10:
        print("password will be too short .")
    else:
        for u in range (user):
            password.append(choice(characters))
    see = "".join(password)
    print(f"your generated password : {see} ")
except ValueError:
    print("enter numerical value for length. eg(1,2,3..etc)")
