nome= input("Digite o nome do funcionário: ")
salario= float (input("Digite o salário do funcionário: "))

if salario < 0:
    salario = salario * - 1
    print("o salário é negativo")

print(f"o salário do funcionário {nome} é {salario} ")