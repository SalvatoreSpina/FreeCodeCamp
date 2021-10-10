import copy
import random
# Consider using the modules imported above.

class Hat:

  def __init__(self, **numbers):
    self.contents=[]
    for key, value in numbers.items():
      for itr in range(value):
        self.contents.append(key)

  def draw(self, amount):
    listap = []
    if amount >= len(self.contents):
      return self.contents
    for i in range(amount):
      nome = self.contents.pop(random.randrange(len(self.contents)))  
      listap.append(nome)
    return listap  

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  conto = 0
  for _ in range(num_experiments):
    temporaneo = copy.deepcopy(hat)
    listatempor = temporaneo.draw(num_balls_drawn)
    successo = True
    for key, value in expected_balls.items():
      if listatempor.count(key) < value:
        successo = False
        break
    if successo:
      conto += 1
      
  return conto / num_experiments        