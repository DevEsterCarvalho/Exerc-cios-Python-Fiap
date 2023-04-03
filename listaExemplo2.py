# criação de exemplos de uma lista com os nomes dos Jedi


jedi = ["Yoda", "Luke", "Obi-Wan", "Anakin"]
# incluindo um valor no final da lista
jedi.append("Mace Windu")
for nome in jedi:
    print(nome)

#ou da seguinte forma


jedi = ["Yoda", "Luke", "Obi-Wan", "Anakin"]
#incluindo um valor digitado no final da lista
jedi.append(input("Digite o nome de um jedi"))
for nome in jedi:
    print(nome)

