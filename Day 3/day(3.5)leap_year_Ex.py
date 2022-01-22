year = int(input("Which year do you wanna check?\n"))
if year % 2 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not leap year")
    else:
        print("Leap Year")
else:
    print("Not leap year")