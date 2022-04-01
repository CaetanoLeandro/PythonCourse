print("#####################################")
print("Bem vindo ao jogo de adivinhação")
print("#####################################")

numero_secreto = 42
total_tentativas = 3
# rodada = 1 # Quando o while é usado

# while (rodada <= total_tentativas):
for rodada in range(1, total_tentativas + 1):
    print("Tentativas {} de {}" .format(rodada, total_tentativas)) # "format" função aplica o valor a  String "{}" (String interpolation)
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

   # rodada = rodada + 1 # Quando o while é usado

print("Fim do jogo")
