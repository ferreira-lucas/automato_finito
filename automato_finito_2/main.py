import operacoes

while 1 == 1:
    print("Simulador de Autômatos:")
    print("1 - Criar um novo autômato;")
    print("2 - Utilizar o autômato criado;")
    print("3 - Mostrar autômato criado;")
    print("4 - Sair.")
    opcao = int(input())

    match opcao:
        case 1:
            operacoes.criaAutomato()
        case 2:
            operacoes.validarPalavra()
        case 3:
            operacoes.mostrarAutomato()
        case 4:
            operacoes.encerrarPrograma()