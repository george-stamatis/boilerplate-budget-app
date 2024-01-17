# This entrypoint file to be used in development. Start by reading README.md
from unittest import main

import budget
from budget import create_spend_chart
food = budget.Category("Food")
entertainment = budget.Category("Entertainment")
business = budget.Category("Business")
'''food.deposit(100, "deposit")
food.transfer(200, entertainment)
food = budget.Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")

clothing = budget.Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
print(food)
print(clothing)

auto = budget.Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)
print(auto)

print(create_spend_chart([food, clothing, auto]))'''
food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
print(create_spend_chart([business, food, entertainment]))
print("Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  ")
#food.deposit(900, "deposit")
#good_withdraw = food.withdraw(45.67)
#actual = food.ledger[1]'''
# Run unit tests automatically
main()