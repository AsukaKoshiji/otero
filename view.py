import tkinter as tk
board = [["." for _ in range(8)] for _ in range(8)]

board[3][3] = "W"
board[3][4] = "B"
board[4][3] = "B"
board[4][4] = "W"

directions = [(0,1), (0,-1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

def place(board, y, x, player):
    if board[y][x] != ".":
        return False

    enemy = "W" if player == "B" else "B"
    can_put = False

    for dy, dx in directions:
        ny, nx = y + dy, x + dx
        cells = []

        while 0 <= ny < 8 and 0 <= nx < 8:
            if board[ny][nx] == enemy:
                cells.append((ny, nx))
            elif board[ny][nx] == player:
                if cells:
                    can_put = True
                break
            else:
                break

            ny += dy
            nx += dx

    if not can_put:
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
    print("クリック：", y, x,)

    if place(board, y, x, player):
        update_board()
        player = "W" if player == "B" else "B"
    else:
        print("置けません")

buttons = []
played = "B"

for y in range(8):      #ボタン
    row = []
    for x in range(8):
        btn = tk.Button(root, text = ".", width = 4, height = 2, command= lambda y=y, x=x: clicked(y, x))
    
        btn.grid(row = y, column = x)
        row.append(btn)
    buttons.append(row)

    
update_board()

root.mainloop()