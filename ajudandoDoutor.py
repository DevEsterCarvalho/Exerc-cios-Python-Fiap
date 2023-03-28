emailAluno = input("Informe o e-mail do aluno")
notaSemestral = input("Informe a nota semestral do aluno: ")

notaSemestral = float(notaSemestral)

if notaSemestral > 8.5:
    print(f"ENVIANDO E-MAIL PARA {emailAluno}")