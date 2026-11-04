
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

print(frota)
