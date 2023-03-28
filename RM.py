rm = input("Infome seu RM:")
idade = input("Informe sua idade: ")
if int (idade) >= 18:
    print(f"Sua participação foi autorizada, aluno de RM {rm}")
    print("Mais informações serão enviadas para seu e-mail cadastrado? ")
else:
    autorizacao = input("Voce possui autorização dos pais para ir? [s/n] ")
    if autorizacao == 's':
        print(f"Sua participação foi autorizada, aluno de rm {rm}")
        print("Mais informações serão enviadas para o e-mail cadastrado! ")
    else:
        print("Sua participação não foi autorizada por causa da idade!")