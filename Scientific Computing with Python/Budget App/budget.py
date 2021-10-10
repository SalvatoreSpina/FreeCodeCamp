class Category:

    def __init__(self, category):
        self.ledger = []
        self.amount = 0
        self.category = category

    def __str__(self):
      output = self.category.center(30, "*") + "\n"
      for item in self.ledger:
        output += f'{item["description"][:23].ljust(23)}{format(item["amount"], ".2f").rjust(7)}\n'
      output += f"Total: {format(self.get_balance(), '.2f')}"
      return output

    def check_funds(self, amount):
        if amount <= self.get_balance():
            return True
        else:
            return False

    def get_balance(self):
      totale = 0
      for item in self.ledger:
        totale += item["amount"]
      return totale

    def deposit(self, amount, description=""):
      self.ledger.append({"amount": amount, "description": description})
    
    def withdraw(self, amount, description=""):
        if self.check_funds(amount) == True:
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def transfer(self, amount, category):        
        if self.check_funds(amount) == True:
            self.ledger.append({"amount": -amount, "description": "Transfer to " + category.category})
            self.amount -= amount
            category.ledger.append({"amount": amount, "description": "Transfer from " + self.category})
            return True
        else:
            return False

def create_spend_chart(categories):
  categoria = []
  spesa = []
  spesaperc = []

  for category in categories:
    total = 0
    for item in category.ledger:
      if item['amount'] < 0:
        total -= item['amount']
    spesa.append(round(total, 2))
    categoria.append(category.category)

  for amount in spesa:
    spesaperc.append(round(amount / sum(spesa), 2)*100)

  graph = "Percentage spent by category\n"

  labels = range(100, -10, -10)

  for label in labels:
    graph += str(label).rjust(3) + "| "
    for percent in spesaperc:
      if percent >= label:
        graph += "o  "
      else:
        graph += "   "
    graph += "\n"

  graph += "    ----" + ("---" * (len(categoria) - 1))
  graph += "\n     "

  longest_name_length = 0

  for name in categoria:
    if longest_name_length < len(name):
      longest_name_length = len(name)

  for i in range(longest_name_length):
    for name in categoria:
      if len(name) > i:
        graph += name[i] + "  "
      else:
        graph += "   "
    if i < longest_name_length-1:
      graph += "\n     "

  return(graph)