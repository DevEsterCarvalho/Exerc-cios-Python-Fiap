quantidade = int(input("Quantos alimentos você consumiu? "))
i = 1
totalCalorias = 0
while (i <= quantidade):
    quantidadeCalorias = float(input(f"Quantas calorias tinha o {i} alimento: "))
    i = i + 1
    totalCalorias = totalCalorias + quantidadeCalorias

print(f"O total de calorias consumidas foram: {totalCalorias}")
