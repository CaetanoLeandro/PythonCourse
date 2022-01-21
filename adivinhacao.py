
print("#####################################")
print("Bem vindo ao jogo de adivinhação")
print("#####################################")

numero_secreto = 42

chute = input("Digite o seu número: ")

print("Voce digitou: ", chute)

chute = int(chute) #converte string >> inteiro

if(numero_secreto == chute):
    print("Você acertou")
else:
    print("Você errou")