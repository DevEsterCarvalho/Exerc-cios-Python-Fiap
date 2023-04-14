batimentos = int(input("Informe o número de batimentos cardiacos por minuto: "))
idade = int(input("Informe sua idade: "))

if idade <= 2:
    if batimentos >= 120 and batimentos <= 140:
        print("Frquencia cardiaca adequada")
    else:
        print("Frequencia cardiaca inadequada")
elif idade >= 8 and idade <= 17:
    if batimentos >= 80 and batimentos <= 100:
        print("Frquencia cardiaca adequada")
    else:
        print("Frequencia cardiaca inadequada")
elif idade >= 18 and idade <= 60:
    if batimentos >= 70 and batimentos <= 80:
        print("Frquencia cardiaca adequada")
    else:
        print("Frequencia cardiaca inadequada")
elif idade >= 60:
    if batimentos >= 50 and batimentos <= 60:
        print("Frquencia cardiaca adequada")
    else:
        print("Frequencia cardiaca inadequada")
else:
    print("Não existe dados para a idade digitada")
