# Dakoda Henley
# 9/15/2026
# P2HW1
# Calculates travel expenses and displays the results in a formatted column layout

print("This program calculates travel expences")
print()
initial_Budget = float(input("Enter initial budget: "))
print()
Destination = input("enter your Destination: ")
print()
Food_expense = float(input("Enter your Food expenses: "))
print()
Accomodations = float(input("Enter cost of Accomodations: "))
print()
Fuel_prices = float(input("Enter your Fuel expenses: "))
print()

# Calculate Leftover Balance
Leftover = initial_Budget - Food_expense - Accomodations - Fuel_prices

# Money values as strings with a dollar sign and 2 decimals
budget_text = f"${initial_Budget:.2f}"
food_text = f"${Food_expense:.2f}"
fuel_text = f"${Fuel_prices:.2f}"
accomodations_text = f"${Accomodations:.2f}"
leftover_text = f"${Leftover:.2f}"

print("------------Travel Expenses------------")

# Every label uses the same width (18) so the values line up
print(f"{'Location:':<18}{Destination}")
print(f"{'Initial Budget:':<18}{budget_text}")
print(f"{'Food Expense:':<18}{food_text}")
print(f"{'Fuel Price:':<18}{fuel_text}")
print(f"{'Accomodations:':<18}{accomodations_text}")

print("---------------------------------------")
print()
print(f"{'Leftover Balance:':<20}{leftover_text}")