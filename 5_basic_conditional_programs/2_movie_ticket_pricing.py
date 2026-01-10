# Problem Statement - Movie tickets are priced based on age
# $12 for adults(18 and over), $8 for children. Everyone
# gets $2 discount on Wednesday

customer_age = int(input("Enter the age:- "))
day = input("Enter the day:- ")

movie_ticket_price = 12 if customer_age >= 18 else 8

if day.lower() == "wednesday":
    movie_ticket_price = movie_ticket_price - 2

print(f"Price of movie:- ${movie_ticket_price}")
