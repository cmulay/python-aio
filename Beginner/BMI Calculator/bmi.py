height = float(input("Enter your height in centimeters: "))
weight = float(input("Enter your Weight in Kg: "))
height /= 100
bmi = weight / (height * height)
print("Your Body Mass Index is: ", bmi)
if bmi > 0:
    if bmi <= 16:
        print("You're severely underweight.")
    elif bmi <= 18.5:
        print("You're underweight.")
    elif bmi <= 25:
        print("You're Healthy.")
    elif bmi <= 30:
        print("You're overweight.")
    else:
        print("You're severely overweight.")
else:
    print("Enter Valid Details")
