print("Welcome to the rollercoster")
height = int(input("Enter your height in cm: "))

if height >= 120:
    print("let me check your age")
    age = int(input("Enter your age: "))
    if age < 12:
        print("pay $7")
    elif age >= 18:
        print("you are good to go. Please pay $10")
    else:
        print("You have to pay $15 more to ride")
else:
    print("Sorry, you have to grow taller before you can ride")