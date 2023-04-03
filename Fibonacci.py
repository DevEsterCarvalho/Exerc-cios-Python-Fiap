numeroUsuario = int(input("informe a quantidade de números para ser checado: "))

anterior1 = 0
anterior2= 1
for numeros in range (1, numeroUsuario + 1, 1):
    numeroAtual = anterior1 +  anterior2
    anterior1 =  anterior2
    anterior2 = numeroAtual
    print(numeroAtual)
    if numeroUsuario == numeroAtual:
        print("Ação bem sucedida!")
        break
    elif numeroUsuario < numeroAtual:
        print("A ação falhou!")
        break

