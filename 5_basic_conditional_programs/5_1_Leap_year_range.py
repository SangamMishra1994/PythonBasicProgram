def count_leap_years(start_year, end_year):
    lower_bound = start_year - 1

    upper_count = (end_year // 4) - (end_year // 100) + (end_year // 400)
    lower_count = (
        (lower_bound // 4)
        - (lower_bound // 100)
        + (lower_bound // 400)
    )

    return upper_count - lower_count


start_year = int(input("Enter starting year: "))
end_year = int(input("Enter end year: "))

count = count_leap_years(start_year, end_year)
print("Total number of leap years are", count)
