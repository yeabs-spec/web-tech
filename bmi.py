name=str(input('insert your name: '))
age=int(input('insert ur age: '))
gender=str(input('insert ur gender (male/female): '))
weight=float(input('insert ur weight in kg: '))
height=float(input('insert ur height in meters: '))

def bmi():
    bmi=weight/(height**2)
    print(bmi)

def bmr_male():
    bmr=88.36 + (13.4 * weight) + (4.8 * height * 100) - (5.7 * age)
    print(bmr)
def bmr_female():
    bmr=447.6 + (9.2 * weight) + (3.1 * height * 100) - (4.3 * age)
    print(bmr)
if gender.lower()=="male":
    bmi()
    bmr_male()
else:
    bmi()
    bmr_female()

    

