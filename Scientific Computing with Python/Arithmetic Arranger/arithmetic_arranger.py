def check (numero1, numero2, operatore):
    try:
      if operatore != "+" and operatore != "-":
        raise BaseException
    except:
      return "Error: Operator must be '+' or '-'."

    try:
      int(numero1)
    except:
      return "Error: Numbers must only contain digits."

    try:
      int(numero2)
    except:
      return "Error: Numbers must only contain digits."

    try:
        if len(numero1) > 4 or len(numero2) > 4:
          raise BaseException
    except:
        return "Error: Numbers cannot be more than four digits."

    return ""

def arithmetic_arranger(problems, mostra=False):

    inizia = True
    sidespace = "    "
    linea1 = linea2 = linea3 = linea4 = ""

    try:
      if len(problems) > 5:
        raise BaseException
    except:
      return "Error: Too many problems."   

    for prob in problems:
      parziale = prob.split()
      numero1 = parziale[0]
      operatore = parziale[1]
      numero2 = parziale[2]
      checks = check(numero1, numero2, operatore)

      if checks != "":
          return checks

      num1 = int(numero1)
      num2 = int(numero2)
      holder = max(len(numero1), len(numero2))

      if inizia == True:
        linea1 += numero1.rjust(holder + 2)
        linea2 += operatore + " " + numero2.rjust(holder)
        linea3 += "-" * (holder + 2)
        if mostra == True:
          if operatore == "+":
            linea4 += str(num1 + num2).rjust(holder + 2)
          else:
            linea4 += str(num1 - num2).rjust(holder + 2)    
        inizia = False

      else:
        linea1 += numero1.rjust(holder + 6)
        linea2 += operatore.rjust(5) + " " + numero2.rjust(holder)
        linea3 += sidespace + "-" * (holder + 2)
        if mostra == True:
          if operatore == "+":
            linea4 += sidespace + str(num1 + num2).rjust(holder + 2)
          else:
            linea4 += sidespace + str(num1 - num2).rjust(holder + 2)

    if mostra == True:
        return linea1 + "\n" + linea2 + "\n" + linea3 + "\n" + linea4

    return linea1 + "\n" + linea2 + "\n" + linea3