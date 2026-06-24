print("Welcome to the tip calculator")
bill_amount = float(input("What is the total bill: "))
tip = float(input("Enter the percentage of the tip(10, 12, 15): "))
tip_per = bill_amount * (tip/100)

Totalbill= bill_amount + tip_per

divide = int(input("How many person you want to divide the bill: "))

print(f"The total bill is: {round(Totalbill, 2)}")
print(f"Bill per person: {round(Totalbill/divide, 2)}")
