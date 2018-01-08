# ask for age
age = input('How old are you? ')
age = int(age)

if age:
  if age >= 18 and age < 21:
    print('You can enter, but you require a wristband')
  elif age >= 21:
    print('You can drink alcohol')
  else:
    print('You are not allowed to come in')
else:
  print('You must enter your age')