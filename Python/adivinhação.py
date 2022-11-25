print("#####################################")
print("# Bem vindo no jogo de Adivinhação! #")
print("#####################################")

numeroSecreto = 42
quantidade_de_tentativas=3

while(quantidade_de_tentativas > 0):
    #Utilizei a interpolação para informar melhor 
    chute = input(f"Você tem {quantidade_de_tentativas} tentativas, Digite o número do chute: ")
    #print("Você digitou", chute)
    chute = int(chute)

    quantidade_de_tentativas -=1
    if (numeroSecreto == int(chute)):
        print("Você acertou!")
        break
    else:
        dica = ""
        if(chute < numeroSecreto ):
            dica = "menor"
        if(chute > numeroSecreto ):
            dica = "maior"
        print("")
        print(f"Você errou, o número {chute} é {dica} do que o número secreto" )
        print("#####################################")