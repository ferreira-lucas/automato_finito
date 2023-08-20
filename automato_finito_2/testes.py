import operacoes

def testeEstadoInicial(estados, initial_state):
    if initial_state in estados:
        operacoes.estado_inicial = initial_state
    else:
        print("Estado inexistente, tente novamente...")

def testeEstadosFinais(estados, final_states):
    teste = 0
    for state in final_states:
        if state in estados:
            teste = 1
    if teste == 0:
        print("Estado inexistente, tente novamente...")
    else:
        for state in final_states:
            operacoes.estados_finais.append(state)

def testeTransicoes(estados, alfabeto, transition):
    teste = 0
    for estado in estados:
        if transition[0] == estado:
            teste = 1
    if teste == 1:
        teste = 0
        for letra in alfabeto:
            if transition[2] == letra:
                teste = 1
        if teste == 1:
            teste = 0
            for estado in estados:
                if transition[1] == estado:
                    teste = 1
            if teste == 1:
                operacoes.func_transicao[(transition[0],transition[2])] = transition[1]
                return 1
            else:
                print("Estado destino inexistente, tente novamente...")
                return 0
        else:
            print("Letra inexistente, tente novamente...")
            return 0
    else:
        print("Estado origem inexistente, tente novamente...")
        return 0