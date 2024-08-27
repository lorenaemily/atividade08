nota = float(input("nota:"))
nome = input("nome:")
disciplina = input("disciplina:")
if nota >= 0 and nota <= 10:
    print ("nota válida. ")
    if nota >= 5.5 and nota < 6:
        nota = 6
    if nota >= 6 and nota <= 10:
        print (f'{nome} está aprovado em {disciplina} com nota {nota}')
    else:
        print (f'{nome} está desaprovado em {disciplina} com nota {nota}')
else:
    print ("nota inválida. ")