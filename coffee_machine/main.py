
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu=Menu()
coffee_maker=CoffeeMaker()
money_machine=MoneyMachine()
items=menu.menu
print("HELLO!! WELCOME!! TODAY'S SPECIAL!!")
for item in items:
    name=item.name
    cost=item.cost
    print(f"{name} : {cost}")
print("\n")    

is_on=True
while is_on:
    print(f"options 1.off 2.report 3.{menu.get_items()}" )
    choice=input("what would you like to do? ")
    if choice=="off":
        is_on=False
    elif choice=="report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink=menu.find_drink(choice)
        if drink not in menu.menu:
            break
        can=coffee_maker.is_resource_sufficient(drink)
        if can==True:
            print("yess!! ingredients are available")
            if money_machine.make_payment(drink.cost):
                print("Payment is successfully done!!")
                coffee_maker.make_coffee(drink)

                

            
    
