# Part 1 - Check Calculation
print('Meal Charge Calculator')
print()

meal_cost = float(input('Enter the cost of your meal: \n'))
tip_percentage = 0.18
tax_percentage = 0.07

tip_amount = meal_cost * tip_percentage
tax_amount = meal_cost * tax_percentage

total_cost = meal_cost + tip_amount + tax_amount
print('Tax (7%):', '${:.2f}'.format(tax_amount))
print('Tip (18%):', '${:.2f}'.format(tip_amount))
print('Your total meal cost with an 18% tip and 7% tax is', '${:.2f}'.format(total_cost))

print()
print()

# Part 2 - Alarm Clock
print('Alarm Clock - 24 Hour Clock')
print()

current_time_hour = int(input('Enter the current hour (in 24-hour format (ex. 2pm -> 14):\n'))
alarm_duration_hours = int(input('In how many hours would you like your alarm to go off?\n'))

clock_hours = 24
alarm_time_hour = (current_time_hour + alarm_duration_hours) % clock_hours

print('Current time:', current_time_hour)
print('Alarm duration:', alarm_duration_hours)
print()
print('Your alarm will go off at', alarm_time_hour)