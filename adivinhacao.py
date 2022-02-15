print("#####################################")
print("Bem vindo ao jogo de adivinhação")
print("#####################################")

numero_secreto = 42
total_tentativas = 3
rodada = 1

while (rodada <= total_tentativas):
    print("Tentativas {} de {}", format(rodada, total_tentativas))
    chute = input("Digite o seu número: ")
    print("Voce digitou: ", chute)
    chute = int(chute)  # converte string >> inteiro

acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto

if (acertou):
    print("Você acertou")

elif (maior):
    print("Você errou! Tente um número menor")

elif (menor):
    print("Você errou! Tente um número menor")

    rodada = rodada + 1

print("Fim do jogo")
