#*******************************************----*Room Rent Mini Project*---------------------***************************

##Input we Need From user's
# Total Rent
# Total Food ordered for Snacking
# Electricity per Unit Spend
# Charge Per Unit
# Persons living in room/flat
## Output
# Total amount you've to pay is

rent = int(input("Enter your hostel/flat rent = "))    # Taking User Input
food = int(input("Enter the amount of food ordered = "))
electricity_spend = int(input("Enter the total of electricity spend = "))
charge_per_unit = int(input("Enter the charge per unit = "))
persons = int(input("Enter the number of persons living in room/flat = "))

total_bill = electricity_spend * charge_per_unit   # Calculating total electricity bill

total_per_person = (food + rent + total_bill) / persons     # Calculating total amount per person
print(f"\nEach person will pay: ₹{total_per_person:.2f}")   # # Displaying the result , # Format to 2 decimal places

# Output:
# Enter your hostel/flat rent = 5000
# Enter the amount of food ordered = 2000
# Enter the total of electricity spend = 100
# Enter the charge per unit = 11
# Enter the number of persons living in room/flat = 2

# Each person will pay: ₹4050.00