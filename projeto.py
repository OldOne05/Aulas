from random import randint

win = 0
lose = 0

cpu = ["Pedra", "Papel", "Tesoura"]
rodadas = int(input("Quantas rodadas você vai jogar?\n"))

while True:
    for i in range(rodadas):
        player = input("Qual sua escolha? [Pedra, Papel, Tesoura]\n").replace(" ","").capitalize()
        pc = randint(0,2)
        print("Eu escolho:")
        print(cpu[pc])
        if player == "Pedra" and cpu[pc] == "Tesoura":
            win += 1
        if player == "Pedra" and cpu[pc] == "Papel":
            lose += 1
        if player == "Tesoura" and cpu[pc] == "Papel":
            win += 1
        if player == "Tesoura" and  cpu[pc] == "Pedra":
            lose += 1
        if player == "Papel" and cpu[pc] == "Pedra":
            win += 1
        if player == "Papel" and cpu[pc] == "Tesoura":
            lose += 1
    if win < lose:
         print("Você perdeu, sou bem melhor que você!! ;)")
    if win > lose:        
        print("Você ganhou, por pura sorte!! >:(")
    if win == lose:            
        print("Empatamos, quer tentar de novo ou está com medo?")
    print(f"Você ganhou {win} rodadas.")
    print(f"Eu ganhei {lose} rodadas.")
    resp = input("Você quer jogar de novo? [S/N]").replace(" ", "").capitalize()
    if resp == "Não":
        break