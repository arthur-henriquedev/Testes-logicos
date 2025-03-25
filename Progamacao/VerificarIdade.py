#Verificar idade do usuário e informar se é criança, adolescente, adulto ou idoso.

while True:
 idade = int(input("Digite a sua idade: "))

 if idade <= 0:
    print("Idade inválida.")
    continue

 elif idade <= 12:
    print("Você é uma criança.")
    break

 elif idade >= 13 and idade <= 18:
    print("Você é um adolescente.")
    break

 elif idade >= 19 and idade <= 59:
    print("Você é um adulto.")
    break

 else:
    print("Você é um idoso.")
    break