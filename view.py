import tkinter as tk
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

def place(board, y, x, player):
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

    board[y][x] = player
    flip(board, y, x, player)
    return True

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

def clicked(y, x):      #クリック処理
    global player

    if place(board, y, x, player):
        update_board()

        player = "W" if player == "B" else "B"
    else:
        print("置けません")

def is_full(board):
    for row in board:
        if "." in row:
            return False
        return True


print_board(board)
if player == "B":
        player = "W"
else:
        player = "B"
    
def counnt_stones(board):       #カウント
        black_count = 0
        white_count = 0
        for row in board:
            for cell in row:
                if cell == "B":
                    black_count += 1
                elif cell == "W":
                    white_count += 1
        return black_count, white_count

def show_result(board):      #結果表示
        black_count, white_count = counnt_stones(board)
        print(f"黒：{black_count}個")
        print(f"白:{white_count}個")
        if black_count > white_count:
            print("黒の勝ちです")
        elif white_count > black_count:
            print("白の勝ちです")
        else:
            print("引き分けです")

buttons = []
played = "B"

for y in range(8):      #ボタン
    row = []
    for x in range(8):
        btn = tk.Button(root, text = ".", width = 4, height = 2, bg = "green", fg = "white", command= lambda y=y, x=x: clicked(y, x))
    
        btn.grid(row = y, column = x)
        row.append(btn)
    buttons.append(row)

    
update_board()

root.mainloop()