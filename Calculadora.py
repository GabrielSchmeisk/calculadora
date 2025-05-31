#By Gabriel Schmeisk

import time
import math

def soma():
    return

def subtracao():
    return 

def multiplicacao():
    return

def divisao():
    return

def porcentagem():
    return

def tabuada():
    return

def raiz():
     return

def imc():
     return
 
def tabela_imc():
    return

def mediaunip():
     return

def perguntar_continuar(funcao):
    while True:
        continuar = input("\nPressione ENTER para fazer outro cálculo, ou digite 'voltar' para voltar ao início:\n").strip().lower()
        if continuar == "":
            funcao()
        elif continuar == "voltar":
            inicio()
            break
        else:
            print("\nVocê não escolheu uma função válida\n")

def inicio():
    while True:
        escolha = input("""
╔═══════════════════════════════════════════╗
║          Selecione uma operação           ║
╠═══════════════════════════════════════════╣
║  1 - Soma                                 ║
║  2 - Subtração                            ║
║  3 - Multiplicação                        ║
║  4 - Divisão                              ║
║  5 - Porcentagem                          ║
║  6 - Tabuadas                             ║
║  7 - Raiz                                 ║
║  8 - IMC                                  ║
║  9 - Média UNIP                           ║
║                                           ║
║  Digite o número da opção desejada:       ║
╚═══════════════════════════════════════════╝
""")
        if escolha == "1":
            soma()
            break
        elif escolha == "2":
            subtracao()
            break
        elif escolha == "3":
            multiplicacao()
            break
        elif escolha == "4":
            divisao()
            break
        elif escolha == "5":
            porcentagem()
            break
        elif escolha == "6":
            tabuada()
            break
        elif escolha == "7":
            raiz()
            break
        elif escolha == "8":
            imc()
            break
        elif escolha == "9":
            mediaunip()
            break
        else:
            print("Você não escolheu uma opção válida 1/2/3/4/5/6/7/8/9, tente novamente!")
            continue

def soma():
    while True:
        try:
            n1 = float(input("Digite o primeiro número da soma: ").replace(",", "."))
            n2 = float(input("Digite o segundo número da soma: ").replace(",", "."))
            break
        except ValueError:
            print("Você deve digitar apenas números válidos!")

    resultado = n1 + n2
    print(f"Resultado parcial: {resultado}")

    while True:
        entrada = input("Digite outro número para somar (ou 'sair' para terminar): ").replace(",", ".").strip().lower()
        if entrada == 'sair':
            break
        try:
            numero = float(entrada)
            resultado += numero
            print(f"Resultado parcial: {resultado}")
        except ValueError:
            print("Digite um número válido ou 'sair' para terminar.")

    print(f"""
╔══════════════════════════════════════╗
║ Resultado final da soma: {resultado}      
╚══════════════════════════════════════╝
""")
    perguntar_continuar(soma)

def subtracao():
    while True:
        try:
            n1 = float(input("Digite o primeiro número da subtração: ").replace(",", "."))
            n2 = float(input("Digite o segundo número da subtração: ").replace(",", "."))
            break
        except ValueError:
            print("\nVocê deve digitar apenas números!\n")

    resultado = n1 - n2
    print(f"Resultado parcial: {resultado}")

    while True:
        entrada = input("Digite outro número para subtrair (ou 'sair' para terminar): ").replace(",", ".").strip().lower()
        if entrada == 'sair':
            break
        try:
            numero = float(entrada)
            resultado -= numero
            print(f"Resultado parcial: {resultado}")
        except ValueError:
            print("Digite um número válido ou 'sair' para terminar.")

    print(f"""
╔═════════════════════════════════════════╗
║ Resultado final da subtração: {resultado}    
╚═════════════════════════════════════════╝
""")
    perguntar_continuar(subtracao)

def multiplicacao():
    while True:
        try:
            n1 = float(input("Digite o primeiro número da multiplicação: ").replace(",", "."))
            n2 = float(input("Digite o segundo número da multiplicação: ").replace(",", "."))
            break
        except ValueError:
            print("\nVocê deve digitar apenas números!\n")

    resultado = n1 * n2
    print(f"Resultado parcial: {resultado}")

    while True:
        entrada = input("Digite outro número para multiplicar (ou 'sair' para terminar): ").replace(",", ".").strip().lower()
        if entrada == 'sair':
            break
        try:
            numero = float(entrada)
            resultado *= numero
            print(f"Resultado parcial: {resultado}")
        except ValueError:
            print("Digite um número válido ou 'sair' para terminar.")

    print(f"""
╔═════════════════════════════════════════════╗
║ Resultado final da multiplicação: {resultado}   
╚═════════════════════════════════════════════╝
""")
    perguntar_continuar(multiplicacao)

def divisao():
    while True:
        try:
            n1 = float(input("Digite o primeiro número da divisão: ").replace(",", "."))
            n2 = float(input("Digite o segundo número da divisão: ").replace(",", "."))
            if n2 == 0:
                print("\nVocê não pode dividir por 0.\n")
                continue
            break
        except ValueError:
            print("\nVocê deve digitar apenas números!\n")

    resultado = n1 / n2
    print(f"Resultado parcial: {resultado}")

    while True:
        entrada = input("Digite outro número para dividir (ou 'sair' para terminar): ").replace(",", ".").strip().lower()
        if entrada == 'sair':
            break
        try:
            numero = float(entrada)
            if numero == 0:
                print("Divisão por zero não é permitida, tente outro número.")
                continue
            resultado /= numero
            print(f"Resultado parcial: {resultado}")
        except ValueError:
            print("Digite um número válido ou 'sair' para terminar.")

        print(f"""
╔══════════════════════════════════════════╗
║ Resultado final da divisão: {resultado}    
╚══════════════════════════════════════════╝
""")
    perguntar_continuar(divisao)

def porcentagem():
        while True:
            try:
                n1 = float(input("Qual a % você quer calcular?:").replace(",", "."))
                n2 = float(input("Número que você deseja saber a %:").replace(",", "."))
            except ValueError:
                    print("\nVocê deve digitar apenas números!\n")
                    continue

            resultado = n1 * n2 / 100

            print(f"""
╔═════════════════════════╗
║ {n1}% de {n2} = {resultado}             
╚═════════════════════════╝
""")

            perguntar_continuar(porcentagem)

def tabuada():
    while True:
        try:
            n1 = int(input("Digite o número da tabuada: "))
            n2 = int(input("Até que número você quer multiplicar? "))
            if n2 > 300:
                print("\nVocê não pode inserir um número maior que 300!\n")
                continue
        except ValueError:
            print("\nVocê deve digitar apenas números!\n")
            continue

        print(f"\nTabuada do {n1} até o número {n2}\n")
        time.sleep(3)

        for i in range(1, n2 + 1): 
            resultado = n1 * i
            print(f"{n1} x {i} = {resultado}")

        while True:
            continuar = input("\nPressione ENTER para fazer outro cálculo, ou digite 'voltar' para voltar ao início:\n").strip().lower()
            if continuar == "":
                break
            elif continuar.lower() == "voltar":
                inicio()
                break
            else:
                print("\nVocê não escolheu uma função válida\n")
            continue

def raiz():
        while True:
            try:
                n1 = float(input("Qual a raiz você quer calcular?:").replace(",", "."))
            except ValueError:
                    print("\nVocê deve digitar apenas números inteiros!\n")
                    continue
            tipo = str(input("Você deseja fazer a raiz quadrada ou cubica?\n\n1 - Quadrada\n2 - Cubica\n"))
            if tipo == "1":
                resultado = round(math.sqrt(n1), 2)
                print(f"""
╔══════════════════════════════════════╗
║ A raiz quadrada de {n1} é {resultado}    
╚══════════════════════════════════════╝
""")

            elif tipo == "2":
                resultado = round(n1 ** (1/3), 2)
                print(f"""
╔══════════════════════════════════════╗
║ A raiz cúbica de {n1} é {resultado}      
╚══════════════════════════════════════╝
""")

            else:
                 print ("Você não escolheu uma opçaõ válida, 1/2. Tente novamente.")
                 continue
            

            perguntar_continuar(raiz)

def imc():
        while True:
            try:
                n1 = float(input("Digite seu peso em quilos:").replace(",", "."))
                n2 = float(input("Digite sua altura em metros:").replace(",", "."))
            except ValueError:
                    print("\nVocê deve digitar apenas números!\n")
                    continue

            resultado = round(n1 / (n2 ** 2), 2)
            if resultado < 16:
                classificacao = "Magreza Grave"
            elif resultado < 17:
                classificacao = "Magreza Moderada"
            elif resultado < 18.5:
                classificacao = "Magreza Leve"
            elif resultado < 25:
                classificacao = "Peso ideal"
            elif resultado < 30:
                classificacao = "Sobrepeso"
            elif resultado < 35:
                classificacao = "Obesidade Grau I"
            elif resultado < 40:
                classificacao = "Obesidade Grau II (severa)"
            else:
                classificacao = "Obesidade Grau III (mórbida)"
                
            print(f"""
╔═══════════════════════════════════════════╗
            Resultado: {resultado}            
         Classificação: {classificacao}      
╚═══════════════════════════════════════════╝
""")

            while True:
                continuar = input("\nPressione ENTER para fazer outro cálculo de IMC, 'IMC' para ver a tabela de cálculo de IMC, ou 'VOLTAR' para voltar ao início:\n").strip().capitalize()
                if continuar == "":
                    break
                elif continuar.lower() == "voltar":
                    inicio()
                    break
                elif continuar.lower() == "imc":
                    tabela_imc()
                    break
                else:
                    print("\nVocê não escolheu uma função válida\n")
                    continue
                
def tabela_imc():
    print("""
╔══════════════════════╦════════════════════════════════╗
║ IMC                  ║ Classificação                  ║
╠══════════════════════╬════════════════════════════════╣
║ Menor que 16         ║ Magreza Grave                  ║
║ 16,0 - 16,9          ║ Magreza Moderada               ║
║ 17,0 - 18,4          ║ Magreza Leve                   ║
║ 18,5 - 24,9          ║ Peso ideal                     ║
║ 25,0 - 29,9          ║ Sobrepeso                      ║
║ 30,0 - 34,9          ║ Obesidade Grau I               ║
║ 35,0 - 39,9          ║ Obesidade Grau II (severa)     ║
║ Maior ou igual a 40  ║ Obesidade Grau III (mórbida)   ║
╚══════════════════════╩════════════════════════════════╝
""")
    
    perguntar_continuar(imc)

def mediaunip():
    while True:
        try:
            np1 = float(input("Digite sua nota da NP1: ").replace(",", "."))
            np2 = float(input("Digite sua nota da NP2: ").replace(",", "."))
            pim = float(input("Digite sua nota do PIM: ").replace(",", "."))
        except ValueError:
            print("\nDigite apenas números válidos!\n")
            continue

        mf = (np1 * 4 + np2 * 4 + pim * 2) / 10

        if mf >= 7:
            print(f"""
╔═══════════════════════════════════════════╗
       Média Final: {mf:.2f} - APROVADO!
╚═══════════════════════════════════════════╝
""")
            continuar = input("Pressione ENTER para novo cálculo ou digite 'SAIR' para retornar ao menu principal:\n").strip().lower()
            if continuar == "sair":
                inicio()
                break
            else:
                continue

        else:
            print(f"""
╔═══════════════════════════════════════════╗
       Média Final: {mf:.2f} - EXAME!
╚═══════════════════════════════════════════╝
""")
            examecalc = input("Você quer calcular sua nota do exame? (SIM/NÃO): ").strip().lower()

            if examecalc == "sim":
                try:
                    exame = float(input("Digite sua nota do exame: ").replace(",", "."))
                except ValueError:
                    print("\nDigite apenas números válidos!\n")
                    continue

                ms = (mf + exame) / 2

                if ms >= 5:
                    print(f"""
╔═══════════════════════════════════════════╗
     Média com Exame: {ms:.2f} - APROVADO!
╚═══════════════════════════════════════════╝
""")
                else:
                    print(f"""
╔══════════════════════════════════════╗
     Média com Exame: {ms:.2f} - DP
╚══════════════════════════════════════╝
""")
            else:
                print("Você escolheu não calcular a nota do exame.")

        perguntar_continuar(mediaunip)

inicio()
