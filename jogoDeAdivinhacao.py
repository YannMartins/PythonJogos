from random import randint
random = randint(1,100)

print("")
print("Boas-vindas! Vamos jogar um jogo de adivinhação?")
print("Adivinhe qual o número escolhido pelo computador entre 1 e 100 em 10 tentativas.")
print("")

tentativa = 0

while tentativa < 10:
    palpite = int(input('Insira o seu palpite: '))
    
    if palpite > random:
        print("Você errou! Dica: seu palpite foi alto.")
        print("")
        tentativa += 1
    elif palpite < random:
        print("Você errou! Dica: seu palpite foi baixo.")
        print("")
        tentativa += 1
    else:
        print("")
        print("Parabéns, você acertou em cheio!")
        print("")
        break;
else:
    print("Você atingiu o número máximo de tentativas! O palpite certo era: {}." .format (random))
    print("")