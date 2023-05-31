def computador_escolhe_jogada(n, m):
    if m > n:
        m = n
    if n == m:
        jogada = n
    elif (m+1) * 2 > n and m < n:
        jogada = n - m - 1
    elif (m+1) * 2 < n:
        jogada = n - (m+1) * (n // (m+1))
    else:
        jogada = m
    if jogada == 0:
        jogada = m
    return jogada


def usuario_escolhe_jogada(n, m):   #jogador informa sua jogada
    valido = False
    while  not valido:
        jogada = int(input("Quantas peças você vai tirar?" ))             
        if jogada > m: 
            valido = False
        elif jogada > n:
            valido = False
        elif jogada <= 0:
            valido = False
        else:
            valido = True
        
        if not valido:
            print("Oops! Jogada inválida! Tente de novo.")
            
    return jogada
        
                                    
def partida():                      #inicia jogo único
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada "))

    print()
    if n % (m+1) == 0:
        print("Você começa!")
        while n > 0:
            jogada = usuario_escolhe_jogada(n, m)
            n = n - jogada
            if jogada == 1:
                print("Você tirou uma peça.\n")
            else:
                print("Você tirou {} peças.\n".format(jogada))
            
            if n == 0:
                return "Fim do jogo! Você ganhou"
            elif n == 1:
                print("Agora resta apenas uma peça no tabuleiro.\n")
            else:
                print("Agora restam {} peças no tabuleiro.\n".format(n))
            jogada = computador_escolhe_jogada(n, m)
            n = n - jogada
            if jogada == 1:
                print("O computador tirou uma peça.\n")
            else:
                print("O computador tirou {} peças.\n".format(jogada))
            
            if n == 0:
                return "Fim do jogo! O computador ganhou!"
            elif n == 1:
                print("Agora resta apenas uma peça no tabuleiro.\n")
            else:
                print("Agora restam {} peças no tabuleiro.\n".format(n))
    else:
        print("Computador começa!")
        while n > 0:
            jogada = computador_escolhe_jogada(n, m)
            n = n - jogada
            if jogada == 1:
                print("O computador tirou uma peça.\n")
            else:
                print("O computador tirou {} peças.\n".format(jogada))
                
            if n == 0:
                return "Fim do jogo! O computador ganhou!"
            elif n == 1:
                print("Agora resta apenas uma peça no tabuleiro.")
            else:
                print("Agora restam {} peças no tabuleiro.".format(n))


            jogada = usuario_escolhe_jogada(n, m)
            n = n - jogada
            if jogada == 1:
                print("Você tirou uma peça.\n")
            else:
                print("Você tirou {} peças.\n".format(jogada))

            if n == 0:
                return "Fim do jogo! Você ganhou"
            elif n == 1:
                print("Agora resta apenas uma peça no tabuleiro.\n")
            else:
                print("Agora restam {} peças no tabuleiro.\n".format(n))


def campeonato():
    i = 1
    CG = 0
    VG = 0
    while i <= 3:
        print("*** Rodada {} ***".format(i))
        ganhador = partida()
        print(ganhador)
        i += 1
        if ganhador == "Fim do jogo! O computador ganhou!":
            CG +=1
        else:
            VG += 1
        
    print("**** Final do campeonato! ****")
    print()
    print("Placar: Você {} X {} Computador".format(VG, CG))


def main():
    print("Bem vindo ao jogo do NIM. Escolha: ")
    decisao = 1
    if decisao == 1 or decisao == 2:
        decisao = int(input("1 - para jogar uma partida isolada \n2 - para jogar um campeonato "))
        if decisao == 1:
            print("Você escolheu uma partida! \n")
            print(partida())
        else:
            print("Você escolheu um campeonato! \n")
            campeonato()
main()                  
              

                                  
