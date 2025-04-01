from colorama import Fore,init
init(autoreset=True)
def base(board):
    print(f"\n {board[0]} | {board[1]} | {board[2]} \n ---|---|--- \n {board[3]} | {board[4]} | {board[5]} \n ---|---|--- \n  {board[6]} | {board[7]} | {board[8]} ")
def XnO(board):
    return[Fore.RED+X+Fore.RESET if X=="X" else Fore.GREEN+X if X=="O" else X for X in board]
def WinCombo(board,symbol):
    conditions=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    return(any(board[a]==board[b]==board[c]==symbol for a,b,c in conditions))
def move(board,symbol,player=True):
    if player:
        while True:
            move1=input("Enter a digit where would you like paste the symbol(1-9) : ")
            if move1.isdigit() and board[int(move1)-1].isdigit():
                board[int(move1)-1]=symbol
                break
    else:
        move1=next((i for i in range(9) if board[i].isdigit() and WinCombo( board[:i]+[symbol]+board[i+1:],symbol)), next((i for i in range(9) if board[i].isdigit()),None))

        board[move1]=symbol

def play():
    print("Welcome to the game, you will be playing against Brainless1234")
    while True:
        board=["1","2","3","4","5","6","7","8","9"]
        player=input("Enter X or O").upper()
        AI="O" if player=="X" else "X"
        turn="player"
        while True:
            base(XnO(board))
            if turn == "player":
                move(board,player)
                if  WinCombo(board,player):
                    print("You defeated the Brainless1234  ")
                    break
            else:
                print("Brainless1234's turn")
                move(board,AI,player=False)
                if WinCombo(board,AI):
                    print("Brainless1234 defeated you")
                    break
            if all(not X.isdigit() for X in board):
                print("Its a tie between you and Brainless1234")
                break
            turn="AI" if turn=="player" else "player"
play()
            

