
def calcularVelocidadeMedia():
    distancia = float(input("Digite a distância percorrida"))
    tempo = float(input("Digite o tempo da viagem"))
    velocidade_media = distancia/tempo
    print(f"A velocidade média é {velocidade_media} km/h")

#inicio programa principal
calcularVelocidadeMedia()