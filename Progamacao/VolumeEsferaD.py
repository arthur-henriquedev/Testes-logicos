#Calcular o volume de uma esfera através do diâmetro

raio = float(input("Digite o raio da esfera: "))

diametro = raio * 2
print("O diâmetro da esfera é: ", diametro)

volume = 3.14159 / 6 * diametro ** 3
print("O volume da esfera é: ", volume)