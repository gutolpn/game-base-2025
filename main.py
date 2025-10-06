import os
import WConio2

#move o cursor para a posição X Y da tela
def gotoxy(x, y):
    print(f"\033[{y};{x}H", end='', flush=True)

#posição do personagem
bichoL = 10
bichoC = 15
inimigoL = 5
inimigoC = 5

#relogio geral
cont =0

#limpa a tela para o jogo começar
os.system('cls')

#construindo tela inicial do jogo
tela = []
for i in range(25):  #vertical        
    tela.append([])
    for j in range(45): #horizontal
        tela[i].append('')

while True:    
    #limpando a matriz do jogo
    for i in range(25):  #vertical        
        for j in range(45): #horizontal
            tela[i][j] = " "

    #colocando os personagens no lugar
    for i in range(25):  #vertical        
        for j in range(45): #horizontal
            if i==bichoL and j==bichoC:
                tela[i][j] = "X"                
                tela[i][j-1] = "X"
                tela[i][j+1] = "X"
                tela[i-1][j] = "X"
            elif i==inimigoL and j==inimigoC:
                tela[i][j] = "O"
                tela[i][j-1] = "O"
                tela[i][j+1] = "O"
                tela[i+1][j] = "O"

            
    #colocando o jogo na tela
    gotoxy(0,0) #posiciona o cursor para escrever
    print("*"*45)
    for i in range(25):  #vertical 
        print("*", end='')       
        for j in range(45): #horizontal
            print(tela[i][j], end='')
        print('*')
    print("*"*45)

    #movendo o inimigo
    if cont % 100 == 0:
        inimigoC += 1

    #atualizo relógio
    cont += 1

    #regra do jogo
    if inimigoC > 43:
        inimigoC = 0

    #interações do usuário
    if WConio2.kbhit():
        codigo, simbolo = WConio2.getch()
        
        #print(codigo, ' ', simbolo)

        match codigo:
            case 72: bichoL -= 1
            case 80: bichoL += 1
            case 77: bichoC += 1
            case 75: bichoC -= 1