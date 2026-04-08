import tkinter as tk
import random

def get_valid_moves(board, player):
    moves = []
    for y in range(8):
        for x in range(8):
            if place(board, y, x, place, True):
                moves.append((y, x))
    return moves

def computer_move():
    global player

    moves = get_valid_moves(board, player)

    if not moves:
        return False
    
    y, x = random.choice(moves)
    place(board, y, x, player)
    return True

def computer_turn():
    global player

    moves = get_valid_moves(board, player)
    if moves:
        y, x = random.choice(moves)
        place(board, y, x, player)
        update_board()
    else:
        print("コンピュータパス")

        player = "B"
        update_status
    
board = [["." for _ in range(8)] for _ in range(8)]

board[3][3] = "W"
board[3][4] = "B"
board[4][3] = "B"
board[4][4] = "W"

directions = [(0,1), (0,-1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

def print_board(board):
    for row in board:
        display = []
        for cell in row:
            if cell == "B":
                display.append("⚫️")
            elif cell == "W":
                display.append("⚪️")
            else:
                display.append(". ")
        print(" ".join(display))


def place(board, y, x, player,check_only = False):
    if board[y][x] != ".":
        return False

    enemy = "W" if player == "B" else "B"
    can_put = False

    for dy, dx in directions:
        ny, nx = y + dy, x + dx
        found_enemy = False

        while 0 <= ny < 8 and 0 <= nx < 8:
            if board[ny][nx] == enemy:
                found_enemy = True

            elif board[ny][nx] == player:
                if found_enemy:
                    can_put = True
                break

            else:
                break

            ny += dy
            nx += dx

    if not can_put:
        return False
    
    if check_only:
        return True

    board[y][x] = player
    flip(board, y, x, player)
    return True

def has_valid_move(board, player):
    for y in range(8):
        for x in range(8):
            if place(board, y, x, player, True):
                return True
    return False

def flip(board, y, x, player):      #ひっくり返す処理
    enemy = "W" if player == "B" else "B"

    for dy,dx in directions:
        ny, nx = y + dy, x + dx
        cells = []

        while 0 <= ny < 8 and 0 <= nx <8:
            if board[ny][nx] == enemy:
                cells.append((ny, nx))

            elif board[ny][nx] == player:
                for cy, cx in cells:
                    board[cy][cx] = player
                break
            else:
                break
            ny += dy
            nx += dx

root = tk.Tk()
root.title("リバーシ")
player = "B"


def update_board():
    for y in range(8):
        for x in range(8):
            if board[y][x] == "B":
                buttons[y][x]["text"] = "⚫️" 
            elif board[y][x] == "W":
                buttons[y][x]["text"] = "⚪️"
            else:
                buttons[y][x]["text"] = " "
#クリック処理
def clicked(y, x):
    global player

#プレイヤー（黒）
    if player != "B":
        return
    if place(board, y, x, player):
        update_board()

        player = "W"
        update_status()

        root.after(500, computer_turn)
    else:
        print("置けません")

#コンピュータ（白）
    if computer_move():
        update_board()
            
        player = "B"
        update_status()

                    # パス処理
    if not has_valid_move(board, player):
        print("パス")
        update_status()

        if not has_valid_move(board, player):
            print("=====ゲーム終了=====")
            show_result(board)
            return
        else:
            print("置けません")

            print("テェック:", player, has_valid_move(board, player))


    update_status()

                
            

buttons = []
played = "B"

for y in range(8):      #ボタン
    row = []
    for x in range(8):
        btn = tk.Button(root, text = ".", width = 4, height = 2, bg = "green", fg = "white", command= lambda y=y, x=x: clicked(y, x))
    
        btn.grid(row = y, column = x)
        row.append(btn)
    buttons.append(row)

status_label = tk.Label(root, text = "黒の番", font = ("Arial", 16))
status_label.grid(row=8, column=0, columnspan=8)


def count_stones(board):       #カウント
    black_count = 0
    white_count = 0
    for row in board:
        for cell in row:
            if cell == "B":
                black_count += 1
            elif cell == "W":
                white_count += 1
    return black_count, white_count

def show_result(board):   #勝敗表示
    black, white = count_stones(board)
        
    if black > white:
        status_label["text"] = f"黒の勝ちです({black} = {white})"
    elif white > black:
        status_label["text"] = f"白の勝ちです({white} = {black})"
    else:
        status_label["text"] = f"引き分けです({black} = {white})"
                  
def update_status():
    if player == "B":
        status_label["text"] = "黒の番"
    else:
        status_label["text"] = "白の番"

    
update_board()

root.mainloop()
