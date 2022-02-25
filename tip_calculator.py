print("Welcome to the tip calculator!\n")
t_bill=float(input("What was the total bill?\n"))
p=int(input("How much tip would you like to give? 10, 12, or,15?\n"))
n=int(input("How many people to split the bill?"))
tip_calculation = p / 100 * t_bill+ t_bill
tip_per_person="{:.2f}".format(tip_calculation/n)
print(f"Each person should  pay  {tip_per_person}")

