import game.funcoes
matriz = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
matrizinvertida = []
matrizauxiliar = []
totvazio = rodadas = 0
circulo = x = empate = False
while True:
    rodadas += 1
    print(f'{"-=" * 30} RODADA {rodadas} {"-=" * 30}')
    game.funcoes.mostraJogo(matriz)
    while True:
        try:
            escolha1l = int(input('Deseja jogar X em que linha? '))
            escolha1c = int(input('Deseja jogar X em que coluna? '))
        except (ValueError, TypeError):
            print(f'\033[31mEsperava-se valores inteiros.\033[m')
        except Exception as erro:
            print(f'\033[31mErro: {erro}\033[m')
        else:
            if 0 <= escolha1l <= 2 and 0 <= escolha1c <= 2:
                if matriz[escolha1l][escolha1c] == ' ':
                    matriz[escolha1l][escolha1c] = 'x'
                    break
                else:
                    print('\033[31mPosição escolhida já foi utilizada!\033[m')
            else:
                print('\033[31mEscolha um número entre 0 e 3, correspondentes as posições da matriz.\033[m')
    process = game.funcoes.processamento(matriz[:], matrizinvertida[:], matrizauxiliar[:])
    if process == 0:
        x = True
        break
    elif process == 1:
        circulo = True
        break
    elif process == 2:
        empate = True
        break
    print(f'{"-=" * 30} RODADA {rodadas} {"-=" * 30}')
    game.funcoes.mostraJogo(matriz)
    while True:
        try:
            escolha2l = int(input('Deseja jogar O em que linha? '))
            escolha2c = int(input('Deseja jogar O em que coluna? '))
        except (ValueError, TypeError):
            print(f'\033[31mEsperava-se valores inteiros.\033[m')
        except Exception as erro:
            print(f'\033[31mErro: {erro}\033[m')
        else:
            if 0 <= escolha2l <= 2 and 0 <= escolha2c <= 2:
                if matriz[escolha2l][escolha2c] == ' ':
                    matriz[escolha2l][escolha2c] = 'o'
                    break
                else:
                    print('\033[31mPosição escolhida já foi utilizada!\033[m')
            else:
                print('\033[31mEscolha um número entre 0 e 3, correspondentes as posições da matriz.\033[m')
    process = game.funcoes.processamento(matriz[:], matrizinvertida[:], matrizauxiliar[:])
    if process == 0:
        x = True
        break
    elif process == 1:
        circulo = True
        break
    elif process == 2:
        empate = True
        break
game.funcoes.mostraJogo(matriz)
print('\033[35m', end='')
if circulo:
    print('O jogador 2 (do círculo) venceu!')
elif x:
    print('O jogador 1 (do x) venceu!')
elif empate:
    print('Empatou!')
else:
    print('Acabou e nem eu sei o porque\033[m')
