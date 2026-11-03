
def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []

    for i in range(tamanho):
        if orientacao == "vertical":
            posicoes.append([linha + i, coluna])
        else:
            posicoes.append([linha, coluna + i])

    return posicoes

def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)

    if nome_navio not in frota:
        frota[nome_navio] = []

    frota[nome_navio].append(posicoes)

    return frota


def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = "X"
    else:
        tabuleiro[linha][coluna] = "-"

    return tabuleiro



def posiciona_frota(frota):
    tabuleiro = []

    for i in range(10):
        tabuleiro.append([0] * 10)

    for tipo in frota:
        for navio in frota[tipo]:
            for posicao in navio:
                linha = posicao[0]
                coluna = posicao[1]
                tabuleiro[linha][coluna] = 1

    return tabuleiro



def afundados(frota, tabuleiro):
    quantidade = 0

    for tipo in frota:
        for navio in frota[tipo]:
            afundou = True

            for posicao in navio:
                linha = posicao[0]
                coluna = posicao[1]

                if tabuleiro[linha][coluna] != "X":
                    afundou = False

            if afundou:
                quantidade = quantidade + 1

    return quantidade
