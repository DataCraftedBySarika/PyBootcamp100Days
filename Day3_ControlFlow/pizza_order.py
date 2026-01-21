print("Welcome to the Pizza Deliveries!")

# Pizza size input
size = input("What size pizza do you want? S, M or L: ").upper()
final_bill = 0

if size == 'S':
    final_bill += 10
elif size == 'M':
    final_bill += 15
elif size == 'L':
    final_bill += 20
else:
    print("Invalid size. Please select the size as per given alphabets")
    exit()

# Pepperoni add-on
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
if pepperoni == 'Y':
    if size == 'S':
        final_bill += 2
    else:
        final_bill += 3
elif pepperoni != 'N':
    print("Invalid choice. Please select Y or N for pepperoni on your pizza")
    exit()

# Extra cheese add-on
extra_cheese = input("Do you want extra cheese on your pizza? Y or N: ").upper()
if extra_cheese == 'Y':
    final_bill += 1
elif extra_cheese != 'N':
    print("Invalid choice. Please select Y or N for extra cheese on your pizza")
    exit()

print(f"Here is the final bill: ${final_bill}")
