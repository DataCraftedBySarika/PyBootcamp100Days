# Day 2 - Tip Calculator Practice

# Greeting
print("Welcome to the Tip Calculator!")

# Get user inputs
bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? "))
people = int(input("How many people to split the bill? "))

# Calculate tip and total amount
tip_amount = tip_percentage / 100
total_tip_amount=bill * tip_amount
total_bill = bill + total_tip_amount

# Split bill
bill_per_person = total_bill / people

# Format result to 2 decimal places
final_amount = round(bill_per_person, 2)

# Display result using f-string
print(f"Each person should pay: ${final_amount:.2f}")

