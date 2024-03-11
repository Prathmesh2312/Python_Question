#Write a Python program to check if a given year is a leap year or not using boolean expressions
def is_leap_year(year):
    return(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

year = int(input("Enter a year:"))
if is_leap_year(year):
    print(year,"is leap year")
else:
    print(year,"is not a leap year")
    