historico = []

banca = float(input("Digite o valor inicial da sua banca: R$ "))
while True:
    print("\n--- Simulador de Banca de Apostas ---")
    print(f"Banca atual: R${banca:.2f}")

    # Pergunta se o usuário quer continuar ou sair
    opcao = input("Deseja fazer uma aposta? (s/n): ")
    if opcao.lower() == "n":
        print("Obrigado por usar o simulador!")
        break

    # Solicita os dados da aposta
    valor_aposta = float(input("Digite o valor da aposta: R$ "))
    odd = float(input("Digite a odd da aposta: "))
    resultado = input("Você ganhou a aposta? (s/n): ")

    # Lógica de atualização da banca
    if resultado.lower() == "s":
        lucro = valor_aposta * (odd - 1)
        banca += lucro
        print(f"Você ganhou R${lucro:.2f}")
    else:
        lucro = -valor_aposta
        banca += lucro  # lucro é negativo aqui
        print(f"Você perdeu R${-lucro:.2f}")

    print(f"Banca atual: R${banca:.2f}")

    # Salvar aposta no histórico
    aposta = {
        "valor": valor_aposta,
        "odd": odd,
        "resultado": "Vitória" if resultado.lower() == "s" else "Derrota",
        "lucro": lucro
    }
    historico.append(aposta)

    # Mostrar histórico de apostas
    print("\n--- Histórico de Apostas ---")
    for i, aposta in enumerate(historico, 1):
        print(f"{i}. Valor: R${aposta['valor']:.2f} | Odd: {aposta['odd']} | Resultado: {aposta['resultado']} | Lucro/Prejuízo: R${aposta['lucro']:.2f}")

