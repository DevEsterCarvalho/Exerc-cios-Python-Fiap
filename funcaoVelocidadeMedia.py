
def calcularVelocidadeMedia(distancia, tempo):
    velocidade_media = distancia/tempo
    return velocidade_media

#inicio programa principal
distancia = float(input("Digite a distância percorrida"))
tempo = float(input("Digite o tempo da viagem"))
print(f"A velocidade média é {calcularVelocidadeMedia(distancia,tempo)} km/h")
