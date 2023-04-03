#lista com valores fora de ordem
valores = [1, 7, 7, 19, 3, 2, 11, 15, 6, 1, 5]
print(f"A lista foi criada assim: {valores}")
#contagem de elementos
contagem = valores.count(7)
print(f"Nessa lista o número 7 aparece {contagem} vezes")

#invertendo a lista
valores.reverse()
print(f"A lista agora está invertida: {valores}")

#ordenando a lista
valores.sort()
print(f"A lista agora está ordenada: {valores}")