op = 1
while op > 0:
   x = input('''           escolha uma operação: 
            1- soma 
            2- subtração
            3- multiplicação
            4- divisão
            5- elevar ao quadrado
            0- sair   
               ''')
   if x == '1':
      n1 = int(input("digite um número: "))
      n2 = int(input("digite outro número: "))
      print(f"{n1}+{n2}={n1+n2}")
   elif x == "2":
      n1 = int(input("digite um número: "))
      n2 = int(input("digite outro número: "))
      print(f"{n1}-{n2}={n1-n2}")
   elif x == "3":
      n1 = int(input("digite um número: "))
      n2 = int(input("digite outro número: "))
      print(f"{n1}x{n2}={n1*n2}")
   elif x == "4":
      n1 = int(input("digite um número: "))
      n2 = int(input("digite outro número: "))
      print(f"{n1}/{n2}={n1/n2}")
   elif x == "5":
      n1 = int(input("digite um número: "))
      print(f"{n1}²={n1**2}") 
   elif x == "0":
      op = 0
   else:
      print("algo deu errado, tente novamente.")