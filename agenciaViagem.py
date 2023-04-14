valorBruto= float(input("Informe o valor bruto da viagem: "))
categoria= input("Informe a categoria:  Economica, Executiva ou Primeira classe")
quantidadeViajantes= int(input("Informe a quantidade de viajantes: "))
desconto= 0
valorLiquido = 0
#convertendo para ler maiusculas ou minusculas
if categoria.upper()== "Economica":
    if quantidadeViajantes == 2:
        desconto = desconto * 0.03
    elif quantidadeViajantes == 3:
        desconto= desconto * 0.04
    elif quantidadeViajantes >4:
        desconto = desconto * 0.05

elif categoria.upper()== "Executiva":
    if quantidadeViajantes == 2:
        desconto = desconto * 0.05
    elif quantidadeViajantes == 3:
        desconto = desconto * 0.07
    elif quantidadeViajantes > 4:
        desconto = desconto * 0.08

elif categoria.upper()== "Primeira classe":
    if quantidadeViajantes == 2:
        desconto = desconto * 0.1
    elif quantidadeViajantes == 3:
        desconto = desconto * 0.15
    elif quantidadeViajantes > 4:
        desconto = desconto * 0.2

else:
    print("Essa categoria não existe")

valorLiquido =  valorBruto- valorLiquido
mediaViajante= valorLiquido/ quantidadeViajantes

print(f"O valor da viagem é {valorBruto} com o desconto de {desconto}, o valor da viagem será de {valorLiquido} e cada viajante tem o custo médio de  {mediaViajante} ")
