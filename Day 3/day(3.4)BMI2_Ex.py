height = float(input("Enter your height: "))
weight = float(input("Enter your weight: "))

bmi = round(weight / height ** 2)

if bmi < 18.5:
    print(f"your BMI is {bmi}, you are underwight.")
elif bmi < 25:
    print(f"your BMI is {bmi}, you are normal.")
elif bmi < 30:
    print(f"your BMI is {bmi}, you are overweight.")
elif bmi < 35:
    print(f"your BMI is {bmi}, you are obese.")
else:
    print(f"your BMI is {bmi}, you are clinically obese.")