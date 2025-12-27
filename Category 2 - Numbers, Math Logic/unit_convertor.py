# =========================================================================
# Write the program to convert kilometers to miles and miles to kilometers
# also include celcius to fahrenheit and fahrenheit to celsius
# =========================================================================


def kilo_to_miles(kilometer):
    return kilometer * 0.621371


def miles_to_kilos(miles):
    return miles / 0.621371


def celsiud_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def farhrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


print("Welcome to the Unit Converter!")
kilo_to_miles_value = float(
    input(
        "Enter value in kilometers to convert to \
miles: "
    )
)
miles = kilo_to_miles(kilo_to_miles_value)
print(f"{kilo_to_miles_value} kilometers is equal to {miles} miles.")
miles_to_kilos_value = float(
    input(
        "Enter value in miles to convert to \
kilometers: "
    )
)
kilometers = miles_to_kilos(miles_to_kilos_value)
print(f"{miles_to_kilos_value} miles is equal to {kilometers} kilometers.")
celsius_value = float(
    input(
        "Enter value in Celsius to convert to Fahrenheit: \
"
    )
)
fahrenheit = celsiud_to_fahrenheit(celsius_value)
print(f"{celsius_value} Celsius is equal to {fahrenheit} Fahrenheit.")
fahrenheit_value = float(
    input(
        "Enter value in Fahrenheit to convert to \
Celsius: "
    )
)
celsius = farhrenheit_to_celsius(fahrenheit_value)
