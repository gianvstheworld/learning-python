import random

def jogar():

    print("********************************")
    print("Bem vindo ao jogo de Adivinhacao")
    print("********************************")

    numero_secreto = random.randrange(1, 101)
    n_tentativas = 0
    pontos = 1000

    print("Qual o nivel de dificuldade?")
    print("(1) Facil (2) Médio (3) Dificil")

    nivel = int(input("Defina o nivel: "))

    if(nivel == 1):
        n_tentativas = 20
    elif(nivel == 2):
        n_tentativas = 10
    else:
        n_tentativas = 5

    for rodada in range(1, n_tentativas + 1):
        print("Tentativa {} de {}".format(rodada,n_tentativas))
        chute_str = input("Digite um numero entre 1 e 100: ")
        print("Voce digitou ", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Voce deve digitar um numero entre 1 e 100")
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Voce acertou e fez {} pontos".format(pontos))
            break
        else:
            if(maior):
                print("Voce errou! O seu chute foi maior do que o numero secreto.")
            elif(menor):
                print("Voce errou! O seu chute foi menor do que o numero secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

if(__name__ == "__main__"):
    jogar()
