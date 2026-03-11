height = float(input("enter your height in m: "))
weight = float (input("enter your weight in kg: "))
BMI = round(weight / height ** 2, 1) 
if BMI < 18.5: 
    print((f"{BMI}you are  underweight"))
elif BMI < 25:
    print(f"{BMI} you are with normal weight!")    
elif BMI < 30:
    print(f"{BMI}you are slightly overweight!")
elif BMI < 35:
    print(f"{BMI}you are obese!!!")
else:
    print(f"your bmi is  {BMI}, you are clinically obese!!")
