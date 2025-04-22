def analisar_ambas_marcam():
    print("\n--- Análise do Mercado: Ambas Marcam ---")
    nota = 0

    pergunta1 = input("Ambas as equipes marcam em mais de 60% dos jogos recentes? (s/n): ")
    if pergunta1.lower() == "s":
        nota += 1

    pergunta2 = input("As defesas dos dois times sofrem muitos gols? (s/n): ")
    if pergunta2.lower() == "s":
        nota += 1

    pergunta3 = input("Os ataques dos dois times têm bom desempenho? (s/n): ")
    if pergunta3.lower() == "s":
        nota += 1

    print("\n>> Resultado da Análise:")
    if nota == 3:
        print("Alta confiança para 'Ambas Marcam'")
    elif nota == 2:
        print("Confiança moderada")
    else:
        print("Baixa confiança. Evite ou aposte com cautela.")

    return nota


# Início do programa
print("Analisador de Apostas : Ambas Marcam ---")

while True:
    print("\nEscolha uma análise:")
    print("1 - Ambas Marcam")
    print("2 - Mais de 1.5 Gols")
    print("3 - Sair")
    print("4 - Analisar mercado Ambas Marcam")

    escolha = input("Digite a opção (1/2/3/4): ")

    if escolha == "1":
        print("\n--- Análise: Ambas Marcam ---")
        time_casa = input("Nome do time da casa: ")
        time_fora = input("Nome do time visitante: ")
        gols_time_casa = int(input(f"{time_casa} marcou em quantos dos últimos 5 jogos? "))
        gols_sofridos_time_fora = int(input(f"{time_fora} sofreu gols em quantos dos últimos 5 jogos? "))
        odd = float(input("Odd para 'Ambas Marcam': "))

        criterio1 = gols_time_casa >= 4
        criterio2 = gols_sofridos_time_fora >= 3
        criterio3 = odd >= 1.50

        if criterio1 and criterio2 and criterio3:
            print(">>> Boa oportunidade para 'Ambas Marcam'!")
        else:
            print(">>> Jogo não recomendado para esse mercado.")

    elif escolha == "2":
        print("\n--- Análise: Mais de 1.5 Gols ---")
        time_casa = input("Nome do time da casa: ")
        time_fora = input("Nome do time visitante: ")
        gols_casa = int(input(f"{time_casa} marcou quantos gols nos últimos 5 jogos? "))
        gols_fora = int(input(f"{time_fora} marcou quantos gols nos últimos 5 jogos? "))
        odd_mais_15 = float(input("Odd para 'Mais de 1.5 gols': "))

        criterio4 = (gols_casa + gols_fora) >= 6
        criterio5 = odd_mais_15 >= 1.30

        if criterio4 and criterio5:
            print(">>> Boa oportunidade para 'Mais de 1.5 gols'!")
        else:
            print(">>> Jogo não recomendado para 'Mais de 1.5 gols'.")

    elif escolha == "4":
        analisar_ambas_marcam()

    elif escolha == "3":
        print("> Fim da análise. Boa sorte nas apostas!")
        break

    else:
        print("Opção inválida. Tente novamente.")
