# check whether fruit is ripe or not based on color
# Green - Unripe, Yellow - ripe, Brown - Overripe

color = input("Enter the color:- ").lower()
result = ""
if color == "green":
    result = "Unripe"
elif color == "yellow":
    result = "Ripe"
else:
    result = "Overripe"
print(f"Banana is {result}")
