print("Você está digitando as notas dos alunos pares")
mediaPar = 0
somaNotasPar = 0

for i in range(2, 48, 2):
    somaNotasPar = somaNotasPar + float(input(f"Por favor, insira a nota do aluno de número {i}: "))
mediaPar = somaNotasPar / 25
print(mediaPar)

print("Você está digitando as notas dos alunos ímpares")
mediaImpar = 0
somaNotasImpar = 0

for i in range (1,49,2):
    somaNotasImpar = somaNotasImpar + float(input(f"Por favor, insita a nota do aluno de número {i}: "))
mediaImpar = somaNotasImpar / 25
print(mediaImpar)

if mediaPar > mediaImpar:
    print("A metade par da sala foi a que teve maior média das notas")
else:
    print("A metade impar da sala foi a que teve maior média das notas")




