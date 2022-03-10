from datetime import date
#print(date.today().day or month or year)
birthYear = int(input('enter year of birth year:'))
currentYear = date.today().year
age = currentYear-birthYear
print('your age is:', age)
print('Today date:',date.today())