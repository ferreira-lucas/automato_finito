import testes
estados = []
alfabeto = []
func_transicao = {}
estado_inicial = ""
estados_finais = []

def criaAutomato():
    global estado_inicial, estados_finais, func_transicao
    estados = []
    alfabeto = []
    func_transicao = {}
    estado_inicial = ""
    estados_finais = []

    print("Informe o alfabeto: ", end="")
    alfabeto = input().split()

    print("Informe a lista de estados: ", end="")
    estados = input().split()

    while estado_inicial == "":
        print("Informe o estado inicial: ", end="")
        retorno = input()
        testes.testeEstadoInicial(estados, retorno)
    #print("PASSOU")

    while estados_finais == []:
        print("Informe os estados finais: ", end="")
        retorno = input().split()
        testes.testeEstadosFinais(estados, retorno)
    #print("PASSOU")

    loop = 0
    while loop == 0:
        print("Informe a transição: ", end="")
        retorno = input().split()
        loop = testes.testeTransicoes(estados, alfabeto, retorno)
        print(func_transicao)
        if loop == 1:
            print("Informar nova transição?")
            print("0 - Sim;")
            print("1 - Não.")
            loop = int(input())
    print(func_transicao)

def validarPalavra():
    print("Informa a palavra à ser validada: ", end="")
    palavra = input()

    estado_atual = estado_inicial

    try:
        for caractere in palavra:
            print("--------------------------")
            print(f"Estado atual: {estado_atual}")
            print(f"Entrada atual: {caractere}")

            print(f"Próximo estado: {func_transicao[(estado_atual, caractere)]}")
            estado_atual = func_transicao[(estado_atual, caractere)]
        
        if estado_atual in estados_finais:
            print("Palavra reconhecida!")
        else:
            print("Palavra não reconhecida!")
    except:
        print("Palavra não reconhecida!")

def mostrarAutomato():
    for estado in estados:
        for letra in alfabeto:
            print(f"({estado}), ({letra}) --> {func_transicao[(estado, letra)]}")

def encerrarPrograma():
    print("Encerrando programa...")
    exit()