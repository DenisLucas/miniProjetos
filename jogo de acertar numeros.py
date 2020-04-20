from random import randint
numero = randint(1, 10)
acertou = False
chances = 4
while not acertou:
    print(f"chute o numero entre 1 e 10, você tem {chances} chances")
    chute = int(input())
    if chute == numero:
        print("acertou")
        acertou = True
    if chute > numero:
        print("muito alto")
        chances = chances - 1
    if chute < numero:
        print("muito baixo")
        chances = chances - 1
    if chances == 0:
        print("suas chances se esgotaram")
        break
