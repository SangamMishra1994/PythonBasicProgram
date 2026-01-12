import datetime
import calendar


def calculate_age(year, month, day):
    dob = datetime.date(year, month, day)
    today = datetime.date.today()

    # Calculate years
    years = today.year - dob.year

    if (today.month, today.day) < (dob.month, dob.day):
        years = years - 1

    #  Calculate months
    months = today.month - dob.month
    if today.day <= dob.day:
        months = months - 1
    if months < 0:
        months = months + 12

    # Calculate Days
    if today.day >= dob.day:
        days = today.day - dob.day
    else:
        prev_month = today.month - 1 or 12
        prev_years = today.year if today.month != 1 else today.year - 1
        days_in_prev_month = calendar.monthrange(prev_years, prev_month)
        days = days_in_prev_month - dob.day + today.day

    return years, months, days


print("Age of the person")
year = int(input("Enter the year:- "))
mont = int(input("Enter the month:- "))
day = int(input("Enter the day:- "))
year, month, day = calculate_age(year, mont, day)
print(f"Years = {year}, month = {month}, days = {day}")
