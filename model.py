def create_board(grid_num):

    board = []
    for x in range(grid_num):
        board.append(["--"] * grid_num)  
    print(" ", " ".join("12345678910"))
    for letter, row in zip("ABCDEFGHIJ", board):
        print(letter, " ".join(row))

print(create_board(5))



    

