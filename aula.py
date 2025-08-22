alturas = []
generos = []

altura = float(input("Digite a altura em metros (ex: 1.75): "))
altura = float(input("Digite a altura em metros (ex: 1.75): "))
altura = float(input("Digite a altura em metros (ex: 1.75): "))
altura = float(input("Digite a altura em metros (ex: 1.75): "))
altura = float(input("Digite a altura em metros (ex: 1.75): "))
altura = float(input("Digite a altura em metros (ex: 1.75): "))
altura = float(input("Digite a altura em metros (ex: 1.75): "))
altura = float(input("Digite a altura em metros (ex: 1.75): "))
altura = float(input("Digite a altura em metros (ex: 1.75): "))
altura = float(input("Digite a altura em metros (ex: 1.75): "))
altura = float(input("Digite a altura em metros (ex: 1.75): "))
altura = float(input("Digite a altura em metros (ex: 1.75): "))
altura = float(input("Digite a altura em metros (ex: 1.75): "))
altura = float(input("Digite a altura em metros (ex: 1.75): "))
altura = float(input("Digite a altura em metros (ex: 1.75): "))

alturas.append(altura)


genero = input("Digite o gênero M ou F : ").upper#colooca em maiusculo btw
genero = input("Digite o gênero M ou F : ").upper
genero = input("Digite o gênero M ou F : ").upper
genero = input("Digite o gênero M ou F : ").upper
genero = input("Digite o gênero M ou F : ").upper
genero = input("Digite o gênero M ou F : ").upper
genero = input("Digite o gênero M ou F : ").upper
genero = input("Digite o gênero M ou F : ").upper
genero = input("Digite o gênero M ou F : ").upper
genero = input("Digite o gênero M ou F : ").upper
genero = input("Digite o gênero M ou F : ").upper
genero = input("Digite o gênero M ou F : ").upper
genero = input("Digite o gênero M ou F : ").upper
genero = input("Digite o gênero M ou F : ").upper
genero = input("Digite o gênero M ou F : ").upper
genero = input("Digite o gênero M ou F : ").upper

generos.append(genero)



soma_alturas_masculino = 0
num_masculino = 0
num_feminino = 0
 
for i in range(len(alturas)):
  
  if generos[i] == 'M':  #varivael i chamando como pessoas p diferenciar masuclino ou feminions
    soma_alturas_masculino += alturas[i]
    num_masculino += 1

  elif generos[i] == 'F':
    num_feminino += 1
    
maior_altura = max(alturas)
menor_altura = min(alturas)
print(f"A maior altura do grupo{maior_altura:}")
print(f"A menor altura do grupo:{menor_altura:}")

if num_masculino > 0:
    media_masculino = soma_alturas_masculino / num_masculino
    print(f"A média de altura do gênero Masculino é: {media_masculino:}")
else :
    print("nao existe pessoas do genero M")

print(f"o numero de pessoas do genero feminino é: {num_feminino}")

#PROF AINDA NAO ACABEI TENTANDO RESOLVER UM BUG
!!
alturas = []
generos = []

for i in range(15):
    altura = float(input(f"Digite a altura da pessoa {i+1} em metros (ex: 1.75): "))
    alturas.append(altura)
    
    genero = input(f"Digite o gênero da pessoa {i+1} M ou F: ").
    while genero not in ['M', 'F']:
        print("genero invalido")
        genero = input(f"digite o genero da pessoa {i+1} M ou F ").
    generos.append(genero)

soma_alturas_masculino = 0
num_masculino = 0
num_feminino = 0

for i in range(len(alturas)):
    if generos[i] == 'M': 
        soma_alturas_masculino += alturas[i]
        num_masculino += 1
    elif generos[i] == 'F':
        num_feminino += 1

maior_altura = max(alturas)
menor_altura = min(alturas)
print(f"A maior altura do grupo é: {maior_altura:} ")
print(f"A menor altura do grupo é: {menor_altura:} ")

if num_masculino > 0:
    media_masculino = soma_alturas_masculino / num_masculino
    print(f"A média de altura do gênero Masculino é: {media_masculino:} ")
else:
    print("Não existem pessoas do gênero M")

print(f"O número de pessoas do gênero feminino é: {num_feminino}")

#CODIGO MAIS SIMPLIFOCADO E CORRRIGIDO PROFESSOR :)
