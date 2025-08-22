
altura = float(input("Digite a sua altura em cms: "))
genero = str(input("digite o seu genero: "))
genero_possivel = "M","F"
if altura in genero_possivel:
    print("altura valida")
else :
    print("altura invalida")
alturas = []
alturas.append(altura)
generos =[]
generos.append(genero)


Media__a_total = alturas / 15 