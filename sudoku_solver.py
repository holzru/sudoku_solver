def sudoku(x):
    board = x[:]
    count = 0
    zeros = sum(a.count(0) for a in board)
    print zeros
    while count < zeros:
        a = 0
        b = 0
        new = 0
        new, a, b = exchange(board)
        board[a][b] = new
        a, b, new = 0, 0, 0
        count += 1
    return board

def exchange(board):
    for c in range(9):
        for d in range(9):
            if board[c][d] == 0 and len(list(set(missing(board, c, d)))) == 9 and 0 in list(set(missing(board, c, d))):
                for e in range(10):
                    if e not in list(set(missing(board, c, d))):
                        return e, c, d
            elif board[c][d] == 0 and len(list(set(missing(board, c, d)))) == 8 and 0 not in list(set(missing(board, c, d))):
                for e in range(1,10):
                    if e not in list(set(missing(board, c, d))):
                        return e, c, d

def missing(lista, coor_a, coor_b):
    box = []
    missing = []
    block(lista, coor_a, coor_b, box)
    for n in range(len(box[0])):
        for x in box[0][n]:
            missing.append(x)
    for x in lista[coor_a]:
        missing.append(x)
    for x in columns(lista, coor_b, missing):
        missing.append(x)
    return missing




def columns(lista, coor, output):
    for x in lista:
        return [x[coor] for x in lista]

def block(lista, coor_a, coor_b, output1):
    b = []
    if coor_a < 3:
        if coor_b < 3:
            b.append(x[:3] for x in lista[:3])
        elif 3 <= coor_b < 6:
            b.append(x[3:6] for x in lista[:3])
        else:
            b.append(x[6:9] for x in lista[:3])
    elif coor_a < 6 and coor_a > 2:
        if coor_b < 3:
            b.append(x[:3] for x in lista[3:6])
        elif 3 <= coor_b < 6:
            b.append(x[3:6] for x in lista[3:6])
        else:
            b.append(x[6:9] for x in lista[3:6])
    else:
        if coor_b < 3:
            b.append(x[:3] for x in lista[6:9])
        elif 3 <= coor_b < 6:
            b.append(x[3:6] for x in lista[6:9])
        else:
            b.append(x[6:9] for x in lista[6:9])
    b = [x for item in b for x in item]
    output1.append(b)





print sudoku([[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]])
