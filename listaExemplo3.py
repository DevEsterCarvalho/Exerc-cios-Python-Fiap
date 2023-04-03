#criação de uma lista com os nomes dos Jedi

jedi = ["Yoda", "Luke", "Obi-Wan", "Anakin"]
#incluindo um valor em uma posição específica da lista
jedi.insert(2, "Luminara")
for nome in jedi:
    print(nome)

#ou da seguinte forma

jedi = ["Yoda", "Luke", "Obi-Wan", "Anakin"]
#incluindo um valor pelo usuário em uma posição específica da lista
jedi.insert(2, input("Digite o nome de um Jedi"))
for nome in jedi:
    print(nome)