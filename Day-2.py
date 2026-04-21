## A simple tip calculator

print("Welcome to the tip calculator! ")
## Takes inputs and converts them
bill_amount = float(input("What was the total bill? $"))
tip_percentage = float(input("How much of a percentage would you like to give for a tip? "))
amount_attending = int(input("How many people will the bill be split between? "))

# calculates the exact tip amount
tip_amount = bill_amount * (tip_percentage / 100)

# provides the bill amount including tip per person
full_bill = tip_amount + bill_amount
bill_per_person = round((full_bill / amount_attending), 2)  ## rounds to the second decimal
print(f"The total bill is for each person is: ${bill_per_person}")

