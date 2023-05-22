#importando modelo sys

import sys

nome = "Ester Carvalho Dias"
idade = 21
peso = 61.500

#Exibindo uma mensagem, nome da variável, o tipo (type) e o tamanho (getsizeof)

print(f"A variável nome é do tipo {type(nome)} e tem {sys.getsizeof(nome)} bytes")
print(f"A variável idade é do tipo {type(idade)} e tem {sys.getsizeof(idade)} bytes")
print(f"A variável peso é do tipo {type(peso)} e tem {sys.getsizeof(peso)} bytes")