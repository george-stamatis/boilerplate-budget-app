class Category:
  def __init__(self, Category):
      self.Category = Category
      self.ledger = []
  def deposit(self, amount, description=""):
      self.ledger.append({"amount": amount, "description": description})
      #print(self.ledger)
  def withdraw(self, amount, description=""):
    #print(self.check_funds(amount))
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
      #print(self.ledger)
      return True
    return False
  def get_balance(self):
    balance = 0
    for transaction in self.ledger:
      balance = balance + transaction["amount"]
    #print("balance:", balance)
    return balance
  def transfer(self, amount, category):
    if self.check_funds(amount):
      self.withdraw(amount, f"Transfer to {category.Category}")
      category.deposit(amount, f"Transfer from {self.Category}")
      return True
    return False
  def check_funds(self, amount):
    if amount > self.get_balance():
      #print("false")
      return False
    return True
  def __str__(self):
    asterisks = (30 - len(self.Category)) // 2
    title_line = f"{'*' * asterisks}{self.Category}{'*' * asterisks}\n"
    output = title_line
    for transaction in self.ledger:
      output += f"{transaction['description'][:23]:23}" + f"{transaction['amount']:>7.2f}\n"
    output += f"Total: {self.get_balance():.2f}"
    return output
  





def create_spend_chart(categories):
  chart = "Percentage spent by category\n"
  spendings = []

  # Calculate the total amount spent for each category
  for category in categories:
      spending = sum(item['amount'] for item in category.ledger if item['amount'] < 0)
      spendings.append(spending)

  # Calculate the percentage spent for each category
  percentages = [(spending / sum(spendings)) * 100 for spending in spendings]

  # Create the bar chart
  for i in range(100, -1, -10):
      chart += str(i).rjust(3) + "| "
      for percent in percentages:
          chart += 'o' if percent >= i else ' '
          chart += '  '
      chart += '\n'

  # Add the horizontal line
  chart += '    ' + '---' * len(categories) + '-' + '\n'

  # Write category names vertically below the bars
  max_name_length = max(len(category.Category) for category in categories)
  for i in range(max_name_length):
      chart += '     '
      for category in categories:
          if i < len(category.Category):
              chart += category.Category[i] + '  '
          else:
              chart += '   '
      chart += '\n'

  return chart.strip()
  