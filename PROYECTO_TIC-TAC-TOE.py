from random import randrange

def DisplayBoard(board):

    """la función acepta un parámetro el cual contiene el estado actual del tablero
    y lo muestra en la consola"""

    print("\n")
    for i in range(3):

        print("+-------+-------+-------+")
        print("|       |       |       |")
        print("|   {}   |   {}   |   {}   |".format(board[i][0],board[i][1],board[i][2],))
        print("|       |       |       |")
        if i==2:
            print("+-------+-------+-------+")

def EnterMove(board,tablero):

    """la función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento, 
    verifica la entrada y actualiza el tablero acorde a la decisión del usuario"""
    

    x=int(input("\nIngrese su movimiento: "))
    if x>0 and x<10:

        i,j=tablero[x]
        if board[i][j]!="X":
            board[i][j]="O"
        return tablero, board
    else:
        print("Ingrese un numero valido(1-9)")
        EnterMove(board,tablero)

def VictoryFor(board,fin):

    """la función analiza el estatus del tablero para verificar si
    el jugador que utiliza las 'O's o las 'X's ha ganado el juego"""

    for i in range(3):
        if board[i][0]==board[i][1]==board[i][2]:
            print("{} ha ganado el juego".format(board[i][0]))
            fin=True
            return fin
    for i in range(3):
        if board[0][i]==board[1][i]==board[2][i]:
            print("{} ha ganado el juego".format(board[0][i]))
            fin=True
            return fin
    if board[0][0]==board[1][1]==board[2][2]:
        print("{} ha ganado el juego".format(board[0][0]))
        fin=True
        return fin
    elif board[2][0]==board[1][1]==board[0][2]:
        print("{} ha ganado el juego".format(board[2][0]))
        fin=True
        return fin
    count=0
    for i in range(3):
        for j in range(3):
            if board[i][j]=="X" or board[i][j]=="O":
                count+=1
                if count==9:
                    print("Empate")
                    fin=True
                    return fin
    return fin

def DrawMove(board):
    """la función dibuja el movimiento de la maquina y actualiza el tablero"""

    movimiento=randrange(1,10)
    i,j=tablero[movimiento]
    if board[i][j]!="O" and board[i][j]!="X":
        board[i][j]="X"
    else:
        DrawMove(board)
    return board

if __name__ == "__main__":
    
    for i in range(1,6):
        print(i*"****")
    print("\nEmpieza el juego")
    print("\nEl PC juega primero:")
    #Crear el tablero
    board=[[1, 2, 3],[4, "X", 6], [7, 8, 9]]
    tablero={1:(0,0), 2:(0,1), 3:(0,2), 4:(1,0), 5:(1,1), 6:(1,2), 7:(2,0), 8:(2,1), 9:(2,2)}
    fin=False
    while not fin:
        DisplayBoard(board)
        EnterMove(board,tablero)
        DisplayBoard(board)
        fin=VictoryFor(board,fin)
        if not fin:
            print("\nTurno maquina: ")
            DrawMove(board)
            DisplayBoard(board)
            fin=VictoryFor(board,fin)

