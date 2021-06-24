per1 = str(input("Você telefonou para a vítima?: [S ou N]\n")).replace(" ", "").capitalize()
per2 = str(input("Você esteve no local do crime?: [S ou N]\n")).replace(" ", "").capitalize()
per3 = str(input("Você mora perto da vítima?: [S ou N]\n")).replace(" ", "").capitalize()
per4 = str(input("Você devia para a vítima?: [S ou N]\n")).replace(" ", "").capitalize()
per5 = str(input("Você já trabalhou para a vítima? [S ou N]:\n")).replace(" ", "").capitalize()

if per1 == "S" and per2 == "S" :
  estadocrim = "Suspeito"
  if per1 == "S" and per2 == "S" and per3 == "S" or per1 == "S" and per2 == "S" and per3 == "S" and per4 == "S" :
    estadocrim = "Cúmplice"
    if per1 == "S" and per2 == "S" and per3 == "S" and per4 == "S" and per5 == "S" :
      estadocrim = "Assassino"
else:
  estadocrim = "Inocente"
print()
print(f"Você é {estadocrim} ")