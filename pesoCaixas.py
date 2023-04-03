#variavel para armazenar o peso total das caixas
pesoTotal = 0.0
#loop para repetir por 100 vezes a solicitação de peso
for x in range(1,101):
    #para cada volta do loop, solicitar o peso da caixa
    pesoAtual = float(input("Informe o peso da caixa atual:"))
    #para cada peso solicitado, somar ao peso total
    pesoTotal = pesoTotal + pesoAtual
#ao final do loop, calcular a média aritmética
media = pesoTotal/100
#exibição dos resultados!
print(f"O peso total de caixas é {pesoTotal}. A média de peso é {media}")