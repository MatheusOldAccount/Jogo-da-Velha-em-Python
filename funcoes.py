def mostraJogo(m):
    for linha in m:
        for pos, coluna in enumerate(linha):
            print(f'{coluna} | ', end='') if pos != 2 else print(f'{coluna}', end='')
        print()
    print()


def processamento(matrizprincipal, matrizinvertida, matrizauxiliar):
    verificar = 0
    for c in range(0, 3):
        if matrizprincipal[c].count(' ') == 0:
            verificar += 1
    if verificar == 3:
        return 2
    diagonalprincipalx = diagonalprincipalo = 0
    diagonalsecundariax = diagonalsecundariao = 0
    for linha in range(0, 3):
        linhax = matrizprincipal[linha].count('x')
        linhao = matrizprincipal[linha].count('o')
        if linhax == 3:
            return 0
        elif linhao == 3:
            return 1
        else:
            for coluna in range(0, 3):
                matrizauxiliar.append(matrizprincipal[coluna][linha])
                if linha == coluna:
                    if matrizprincipal[linha][coluna] == 'x':
                        diagonalprincipalx += 1
                    elif matrizprincipal[linha][coluna] == 'o':
                        diagonalprincipalo += 1
                if (linha + coluna) == 2:
                    if matrizprincipal[linha][coluna] == 'x':
                        diagonalsecundariax += 1
                    elif matrizprincipal[linha][coluna] == 'o':
                        diagonalsecundariao += 1
            matrizinvertida.append(matrizauxiliar[:])
            matrizauxiliar.clear()
        linhax2 = matrizinvertida[linha].count('x')
        linhao2 = matrizinvertida[linha].count('o')
        if linhax2 == 3:
            return 0
        elif linhao2 == 3:
            return 1
    if diagonalprincipalx == 3 or diagonalsecundariax == 3:
        return 0
    if diagonalprincipalo == 3 or diagonalsecundariao == 3:
        return 1
    else:
        return 10

