'''
year = int(input('Choose a year: '))
def is_leap(year):
    leap = False
    
    if year / 4 == 0:
        print(True) 
    else:
        print(False)
'''      

'''
year = 1990
leap_year = year / 4 
leap2_year = year / 400
if leap_year % 4 == 0:
    print('Leap year')
else:
    print('Normal year')
    
print(leap_year)
'''
'''
#Forma 1
year = int(input('Choose a year: '))

def is_leap(year):
    leap = True
    if year%4==0 and year % 100 != 0 or year % 400 == 0:
        return leap
    else:
        return not leap
        
print(is_leap(year))
'''


#Forma 2
import calendar
def is_leap(year):
    leap = calendar.isleap(year)
    return leap
year = int(input('choose year: '))
print(is_leap(year))
