segunda = int(input("Quantos votos a segunda-feira recebeu? "))
terca = int(input("Quantos votos a terça-feira recebeu? "))
quarta = int(input("Quantos votos a quarta-feira recebeu? "))
quinta = int(input("Quantos votos a quinta-feira recebeu? "))
sexta = int(input("Quantos votos a sexta-feira recebeu? "))

if segunda > terca and segunda > quarta and segunda > quinta and segunda > sexta:
    print(f"O dia escolhido foi segunda-feira {segunda} votos")
elif terca > segunda and terca > quarta and terca > quinta and terca > sexta:
    print(f"O dia escolhido foi terça-feira {terca} votos")
elif quarta > segunda and quarta > terca and quarta > quinta and quarta > sexta:
    print(f"O dia escolhido foi quarta-feira com {quarta} votos")
elif quinta > segunda and quinta > terca and quinta > quarta and quinta > sexta:
    print(f"O dia escolhido foi quinta-feira {quinta} votos")
elif sexta > segunda and sexta > terca and sexta > quarta and sexta > quinta:
    print(f"O dia escolhido foi sexta-feira {sexta} votos")
