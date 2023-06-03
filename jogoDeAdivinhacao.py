from random import randint
random = randint(1,100)

print("\nBoas-vindas! Vamos jogar um jogo de adivinhação?")
print("Adivinhe qual o número escolhido pelo computador entre 1 e 100 em 10 tentativas.\n")

tentativa = 1

while tentativa < 11:
    print(f"TENTATIVA {tentativa} DE 10")
    palpite = int(input('Insira o seu palpite: '))
    
    if palpite > random:
        print("Você errou! Dica: seu palpite foi alto.\n")
        tentativa += 1
    elif palpite < random:
        print("Você errou! Dica: seu palpite foi baixo.\n")
        tentativa += 1
    else:
        print("\nParabéns, você acertou em cheio!\n")
        break;
else:
    print(f"Você atingiu o número máximo de tentativas! O palpite certo era: {random}.\n")
