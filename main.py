Weight = int(input('What is your weight, in pounds?'))
Height = int(input('What is you height, in inches?'))
conversionWeight = Weight * 0.45
conversionHeight = Height * 0.025
squareHeight = conversionHeight * conversionHeight
bodyMassIndex = conversionWeight / squareHeight
print(f'Your body mass index is {bodyMassIndex}.')
if bodyMassIndex < 18.5:
    print("You are under weight. Try to eat more!")
elif 18.5 <= bodyMassIndex <= 24.9:
    print("You have a normal BMI. Keep up the good work!")
elif 25 <= bodyMassIndex <= 29.9:
    print("You are overweight! Eat healthier!")
elif bodyMassIndex > 30:
    print("You are obese! You really need to watch your diet. No more soda and candy!")