# Инициализация игровой доски
board = [1,2,3,4,5,6,7,8,9]

# Инициализация победных линий
victories = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

def print_board():
    '''вывод игровой доски на экран'''
    print(*board[0:3], sep = " ")
    print(*board[3:6], sep = " ")
    print(*board[6:9], sep = " ")
    # print(*[f'{board[i:i+3]}, \n' for i in range(0, 9, 3)])

def step_board(step_id,symbol):
    '''Заменяет числовое значение позиции (если она свободна) на символ'''
    if isinstance(board[step_id-1],int):
        board[step_id-1] = symbol
    else:
        step_id = int(input("Позиция уже занята. Ваш ход: "))
        step_board(step_id,symbol)

def get_result():
    '''Получить текущий результат игры'''
    win = ""
    for i in victories:
        if board[i[0]] == board[i[1]] == board[i[2]] == "X":
            win = "X"
        if board[i[0]] == board[i[1]] == board[i[2]] == "O":
            win = "O"
    win_flag = False
    for j in range(0,len(board)):
        if isinstance(board[j],int):
            win_flag = True
    if win_flag == False:
        win = "N"
    return win

# Процесс игры
game_over = False
player1 = True
while game_over == False:
    print_board()
    if player1 == True:
        symbol = "X"
        step_id = int(input("Игрок 1, ваш ход: "))
    else:
        symbol = "O"
        step_id = int(input("Игрок 2, ваш ход: "))
    # board[step_id-1] = symbol
    step_board(step_id, symbol)
    win = get_result()
    if win != "":
        game_over = True
    else:
        game_over = False
    player1 = not(player1)

# Игра окончена. Печатаем результат
print_board()
if win == "X":
    print("Победил игрок 1")
elif win == "O":
    print("Победил игрок 2")
elif win == "N":
    print("Ничья")