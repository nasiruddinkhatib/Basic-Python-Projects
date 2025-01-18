# Initialize the bill to 0
bill = 0
# Case-Insensitive Input: .strip().upper() ensures the program accepts inputs like " s ", "M", or "l".
size = input("What is the Size Of Pizza You Want (S, M, L)? ").strip().upper()
# Determine the cost based on the pizza size
if size == 'S':  # Small pizza
    bill += 100
    print("Small Pizza Price is 100 Rs.")
elif size == 'M':  # Medium pizza
    bill += 200
    print("Medium Pizza Price is 200 Rs.")
elif size == 'L':  # Large pizza
    bill += 300
    print("Large Pizza Price is 300 Rs.")
else:
    # Exit if the user enters an invalid size
    print("Invalid input. Please select a proper size (S, M, L).")
    exit()
# Ask the user if they want pepperoni and standardize the input
add_pepperoni = input("Do you want Pepperoni (Y/N)? ").strip().upper()

# Determine the additional cost for pepperoni based on the pizza size
if add_pepperoni == 'Y':  # If the user wants pepperoni
    if size == 'S':  # Add 30 Rs for small pizza
        bill += 30
    else:  # Add 50 Rs for medium or large pizza
        bill += 50
elif add_pepperoni != 'N':  # Check for invalid input
    print("Invalid input. Please enter Y or N for Pepperoni.")
    exit()

# Ask the user if they want extra cheese and standardize the input
extra_cheese = input("Do you want Extra Cheese (Y/N)? ").strip().upper()

# Add the cost for extra cheese if the user wants it
if extra_cheese == 'Y':  # Add 20 Rs for extra cheese
    bill += 20
elif extra_cheese != 'N':  # Check for invalid input
    print("Invalid input. Please enter Y or N for Extra Cheese.")
    exit()

# Print the final bill after all inputs
print(f"Your Final Bill is {bill} Rs.")
