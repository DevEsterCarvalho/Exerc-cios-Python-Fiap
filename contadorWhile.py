n= int(input("De qual número quer a tabuada? "))
contador = 1

while (contador <= 10):
    print("{} * x {} = {}".format(n, contador, n * contador))
    contador = contador + 1