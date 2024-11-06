
#practical no.5
name = "kalyani"

i = 0
empty =""
while i < len(name):
    if name[i] not in empty:
          print(f"{name[i]} : {name.count(name[i])}")
    empty += name[i]
    i += 1

