nome = input("nome: ")
disciplina = input("disciplina: ")
nota = float(input("nota: "))
if nota >= 0 and nota <=10:
    print("nota válida. ")
    if nota >= 5.5 and nota < 6:
        nota = 6
    if nota >= 6:
        print (f'{nome} está aprovado em {disciplina} com {nota}')
    else:
        print ("reprovado")
else:
    print("nota inválida. ")
