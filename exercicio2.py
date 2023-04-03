quantidadeTransacoes = int(input("Quantas transações você realizou hoje? "))
totalTransacao = 0
for numeroTransacoes in range(1, quantidadeTransacoes + 1, 1):
    valorTransacao = float(input("Por favor, informe o valor de cada transação: "))
    totalTransacao = totalTransacao + valorTransacao
    media = totalTransacao / numeroTransacoes

print(f"O número de transações foram {numeroTransacoes}, o valor total foi {totalTransacao} e a media foi de {media}")