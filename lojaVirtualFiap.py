
valorCompra = input("Informe o valor da compra realizada ")
cupom = input("Digite o cupom de desconto ")

if cupom.upper() == "NIVER10":
    valorFinal = float(valorCompra) * 0.9
else:
    valorFinal = float(valorCompra)
    print("CUPOM INVÁLIDO")

print(f"O valor final da compra é {valorFinal}")