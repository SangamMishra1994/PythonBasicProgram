import math
from decimal import Decimal, ROUND_HALF_UP


def calculate_area_and_circumference(radius):
    area = math.pi * radius**2
    circumference = 2 * math.pi * radius
    return area, circumference


a, c = calculate_area_and_circumference(7)
print(f"Area = {a:.3f}\nCircumference = {c:.3f}")
print(format(a, ".2f"), format(c, ".3f"))

print(Decimal(a).quantize(Decimal("0.00"), rounding=ROUND_HALF_UP))
