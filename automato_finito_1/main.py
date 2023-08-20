estados = []
alfabeto = []
func_transicao = {}
estado_inicial = ""
estados_finais = []

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

print("Informe o estado inicial: ", end="")
estado_inicial = input()

print("Informe o alfabeto: ", end="")
alfabeto = input().split()

print("Informe a lista de estados: ", end="")
estados = input().split()

print("Informe os estados finais: ", end="")
estados_finais = input().split()

loop = 0
while loop == 0:
    print("Informe a transição (Digitar . para terminar): ", end="")
    retorno = input().split()
    if retorno == ['.']:
        loop = 1
    else:
        func_transicao[(retorno[0],retorno[2])] = retorno[1]
        retorno = []

validarPalavra()