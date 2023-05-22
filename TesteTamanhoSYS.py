#importando modelo sys

import sys

nome = "Ester Carvalho Dias"
idade = 21
peso = 61.500

#Exibindo uma mensagem, nome da variável, o tipo (type) e o tamanho (getsizeof)

print("A variável nome é do tipo {} e tem {} bytes".format(type(nome), sys.getsizeof(nome)))
print("A variável idade é do tipo {} e tem {} bytes".format(type(idade), sys.getsizeof(idade)))
print("A variável peso é do tipo {} e tem {} bytes".format(type(peso), sys.getsizeof(peso)))