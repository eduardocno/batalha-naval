
from funcoes import define_posicoes, preenche_frota, posicao_valida

frota = {}

navios = {
    "porta-aviões": [4, 1],
    "navio-tanque": [3, 2],
    "contratorpedeiro": [2, 3],
    "submarino": [1, 4]
}

for nome in navios:
    tamanho = navios[nome][0]
    quantidade = navios[nome][1]

    for i in range(quantidade):
        valido = False

        while valido == False:
            print("Insira as informações referentes ao navio", nome, "que possui tamanho", tamanho)

            linha = int(input("Linha: "))
            coluna = int(input("Coluna: "))

            if nome == "submarino":
                orientacao = "vertical"
            else:
                escolha = int(input("[1] Vertical [2] Horizontal >"))

                if escolha == 1:
                    orientacao = "vertical"
                else:
                    orientacao = "horizontal"

            valido = posicao_valida(frota, linha, coluna, orientacao, tamanho)

            if valido == False:
                print("Esta posição não está válida!")
            else:
                posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
                frota = preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)


from funcoes import posiciona_frota, faz_jogada, afundados

frota_oponente = {
    "porta-aviões": [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    "navio-tanque": [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    "contratorpedeiro": [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    "submarino": [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tabuleiro_jogador = posiciona_frota(frota)
tabuleiro_oponente = posiciona_frota(frota_oponente)


def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '    0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += ' _______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([str(info) if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'

    return texto


jogando = True

while jogando:
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    linha = int(input("Jogador, qual linha deseja atacar? "))

    while linha < 0 or linha > 9:
        print("Linha inválida!")
        linha = int(input("Jogador, qual linha deseja atacar? "))

    coluna = int(input("Jogador, qual coluna deseja atacar? "))

    while coluna < 0 or coluna > 9:
        print("Coluna inválida!")
        coluna = int(input("Jogador, qual coluna deseja atacar? "))

    while tabuleiro_oponente[linha][coluna] == "X" or tabuleiro_oponente[linha][coluna] == "-":
        print("A posição linha", linha, "e coluna", coluna, "já foi informada anteriormente!")

        linha = int(input("Jogador, qual linha deseja atacar? "))

        while linha < 0 or linha > 9:
            print("Linha inválida!")
            linha = int(input("Jogador, qual linha deseja atacar? "))

        coluna = int(input("Jogador, qual coluna deseja atacar? "))

        while coluna < 0 or coluna > 9:
            print("Coluna inválida!")
            coluna = int(input("Jogador, qual coluna deseja atacar? "))

    tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha, coluna)

    quantidade = afundados(frota_oponente, tabuleiro_oponente)

    if quantidade == 10:
        print("Parabéns! Você derrubou todos os navios do seu oponente!")
        jogando = False

