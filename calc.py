#programa com as 4 operações matemáticas, para que seja criado um módulo
#soma
def somar(a, b):
    return float(a) + float(b)

#subtração
def subtrair(a, b):
    return float(a) - float(b)

#divisão
def dividir(a, b):
    if b==0:
        return 0
    return float(a) / float(b)

#multiplicação
def multiplicar(a, b):
          return float(a) * float(b)