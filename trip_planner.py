print("=== Road Trip Planner ===")
destination = input("Enter destination: ")
distance = input("Total distance in miles: ")
distance = float(distance)

mpg = input("Car MPG: ")
mpg = float(mpg)

gas_price = input("Current Gas Price per gallon: ")
gas_price = float(gas_price)

number_of_nights = input("How many nights stayed: ")
number_of_nights = int(number_of_nights)

hotel_cost = input("Average Hotel Cost per night: ")
hotel_cost = float(hotel_cost)

food_budget = input("Daily food budget: ")
food_budget = float(food_budget)

gallons = (distance / mpg)
total_gas_cost = (gallons * gas_price)
total_hotel_cost = (number_of_nights * hotel_cost)
total_food_cost = (number_of_nights + 1) * (food_budget)
grand_total = (total_gas_cost + total_food_cost + total_hotel_cost)

print()
print(f"Destination: {destination}")
print(f"Distance: {distance:.2f}")

print()
print("--- COST BREAKDOWN ---")

print(f"Gas ({gallons:.2f} gal @ ${gas_price:.2f}/gal): ${total_gas_cost:.2f}")
print(f"Hotel ({number_of_nights:.2f} nights @ ${hotel_cost:.2f}): ${total_hotel_cost:.2f}")
print(f"Food ({number_of_nights + 1} days @ ${food_budget:.2f}): ${total_food_cost:.2f}")

print("=" * 35)
print(f"Estimated Total: ${grand_total:.2f}")





      


