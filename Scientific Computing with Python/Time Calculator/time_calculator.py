def add_time(start, duration, day=None):

  giornilist = {
        "Saturday": 0,
        "Sunday": 1,
        "Monday": 2,
        "Tuesday": 3,
        "Wednesday": 4,
        "Thursday": 5,
        "Friday": 6
    }

  start = start.split()
  orariostart = start[0]
  formatostart = start[1]
  parzialestart = orariostart.split(":")
  orestart = parzialestart[0]
  minutistart = parzialestart[1]
  intorestart = int(orestart)
  intminutistart = int(minutistart)

  duration = duration.split(":")
  oreduration = duration[0]
  minutiduration = duration[1]
  intoreduration = int(oreduration)
  intminutiduration = int(minutiduration)

  if formatostart == "AM":
    ore = intorestart + intoreduration  
    minuti = intminutistart + intminutiduration
  elif formatostart == "PM":
    ore = intorestart + intoreduration + 12
    minuti = intminutistart + intminutiduration

  minutiecc = int(minuti) // 60
  minuti = int(minuti) % 60
  ore = ore + minutiecc
  
  oreecc = int(ore) // 24
  ore = int(ore) % 24

  if minuti < 10:
    minuti = str("0" + str(minuti))

  if ore > 11:
    ore = int(ore) - 12
    formato = "PM"
  else:
    formato = "AM"

  if ore == 0:
    ore = 12

  if day != None:
    
    giornop = (giornilist[day.lower().capitalize()] + oreecc) % 7
    for i, j in giornilist.items():
      if j == giornop:
        giornop = i
        break

    if oreecc == 1:
      new_time = str(ore) + ":" + str(minuti) + " " + formato + ", " + str(giornop) + " (next day)"

    elif oreecc > 1:
      new_time = str(ore) + ":" + str(minuti) + " " + formato + ", " + str(giornop) + " (" + str(oreecc) + " days later)" 

    else:  
      new_time = str(ore) + ":" + str(minuti) + " " + formato + ", " + str(giornop)

  else:

    if oreecc == 1:
      new_time = str(ore) + ":" + str(minuti) + " " + formato + " (next day)" 

    elif oreecc > 1:
      new_time = str(ore) + ":" + str(minuti) + " " + formato + " (" + str(oreecc) + " days later)" 

    else:  
      new_time = str(ore) + ":" + str(minuti) + " " + formato

  return new_time
