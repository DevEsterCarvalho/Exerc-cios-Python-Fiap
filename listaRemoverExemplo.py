#criação de uma lista com os nomes dos Jedi

jedi = ["Yoda", "Luke", "Obi-Wan", "Anakin"]
#Removendo o último valor inserido na lista
jedi.pop()
for nome in jedi:
    print(nome)

#ou da seguinte forma

jedi = ["Yoda", "Luke", "Obi-Wan", "Anakin"]
#Removendo um valor em uma posição específica
jedi.pop(2)
for nome in jedi:
    print(nome)

#ou da seguinte forma

jedi = ["Yoda", "Luke", "Obi-Wan", "Anakin"]
#Removendo um valor específico da lista
jedi.remove("Yoda")
for nome in jedi:
    print(nome)