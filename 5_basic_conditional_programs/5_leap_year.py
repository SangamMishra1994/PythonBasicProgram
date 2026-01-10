# Write a program to check the leap year
year = int(input("Enter the year:- "))
# if year is divisible by 400 and 100 both then its
# a leap year
if (year % 400 == 0) and (year % 100 == 0):
    print(f"{year} is a leap year.")
# Year is divisible by 4 is leap year
# not divisible by 100 it is not century year
elif (year % 4 == 0) and (year % 100 != 0):
    print(f"{year} is a leap year.")
# year not divisble by 4 is not leap year
else:
    print(f"{year} is not a leap year.")
