height = input("Enter your height in m: ")
weight = (input("Enter your weight in kg: "))

a = float(height ** 2)

bmi = int(weight) / float(height) ** 2
bmi = int(bmi)

print("Your BMI is " + str(bmi))