voto1 = input("Informe qual o prêmio que quer receber: Playstation, Xbox ou Nintendo ")
voto2 = input("Informe qual o prêmio que quer receber: Playstation, Xbox ou Nintendo ")
voto3 = input("Informe qual o prêmio que quer receber: Playstation, Xbox ou Nintendo ")
voto4 = input("Informe qual o prêmio que quer receber: Playstation, Xbox ou Nintendo ")
voto5 = input("Informe qual o prêmio que quer receber: Playstation, Xbox ou Nintendo ")

playstation = 0
xbox = 0
nintendo = 0

if voto1.upper() == "Playstation":
    playstation = playstation + 1
elif voto1.upper() == "xbox":
    xbox = xbox + 1
elif voto1.upper() == "nintendo":
    nintendo = nintendo + 1

if voto2.upper() == "Playstation":
    playstation = playstation + 1
elif voto2.upper() == "xbox":
    xbox = xbox + 1
elif voto2.upper() == "nintendo":
    nintendo = nintendo + 1

if voto3.upper() == "Playstation":
    playstation = playstation + 1
elif voto3.upper() == "xbox":
    xbox = xbox + 1
elif voto3.upper() == "nintendo":
    nintendo = nintendo + 1

if voto4.upper() == "Playstation":
    playstation = playstation + 1
elif voto4.upper() == "xbox":
    xbox = xbox + 1
elif voto4.upper() == "nintendo":
    nintendo = nintendo + 1

if voto5.upper() == "Playstation":
    playstation = playstation + 1
elif voto5.upper() == "xbox":
    xbox = xbox + 1
elif voto5.upper() == "nintendo":
    nintendo = nintendo + 1
if playstation > xbox and playstation > nintendo:
    print("o prêmio escolhido foi playstation")
elif xbox > playstation and xbox > nintendo:
    print("O prêmio escolhido foi o xbox")
elif nintendo > playstation and nintendo > xbox:
    print("o prêmio escolhido foi nintendo")
else :
    print("Houve empate")