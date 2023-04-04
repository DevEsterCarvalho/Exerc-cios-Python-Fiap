tipoAssinatura = input("Qual é o nível da sua assinatura? (Basic, Silver, Gold ou Platinum) ")
faturamentoAnual = float(input("Qual é o seu faturamento anual? "))

porcentagem = 0
bonus = 0

if tipoAssinatura == "basic":
    porcentagem =  faturamentoAnual - faturamentoAnual*30/100
elif tipoAssinatura == "silver":
    porcentagem = faturamentoAnual - faturamentoAnual*20/100
elif tipoAssinatura == "gold":
    porcentagem = faturamentoAnual - faturamentoAnual*10/100
elif tipoAssinatura == "platinum":
    porcentagem = faturamentoAnual - faturamentoAnual*5/100
bonus = faturamentoAnual - porcentagem

print(f"O bônus que o cliente deve pagar para o curso de Produção Multimídia do FIAP ON é {bonus}")