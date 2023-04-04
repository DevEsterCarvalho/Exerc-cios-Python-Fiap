minutos = int(input("Quais são os minutos atuais? "))

resposta = 1
contador = 1

while contador <= minutos:
    resposta = resposta * contador
    contador = contador + 1

print(f"A senha é: Liberdade{resposta}")