def main():
    with open("input.ini") as f:
       data = [i for i in f.read().splitlines()]

    draw_numbers = [i for i in data[0].split(",")]
    boards = []
    winners = []

    # Create Boards
    for num, val in enumerate(data):
        if (num + 4) % 6 == 0:
            boards.append([val.split(), data[num + 1].split(), data[num + 2].split(), data[num + 3].split(), data[num + 4].split()])
    
    # Mark centre as free-space
    # for board in boards:
    #     board[2][2] = 'X'

    # Draw numbers
    for draw in draw_numbers:
        for j, board in enumerate(boards):
            for k, row in enumerate(board):
                for l, coord in enumerate(row):
                    if draw == coord and j not in winners:
                        boards[j][k][l] = 'X'

        # Search for Bingo
        for board_index, board in enumerate(boards):
            # rows
            for row in board:
                count_rows = 0
                for coord in row:
                    if coord == 'X':
                        count_rows += 1
                if count_rows == 5 and board_index not in winners:
                    winners.append(board_index)
                    print("number drawn: " + str(draw))
                    print("board " + str(board_index + 1) + " has horizontal bingo")

                    last_winner_draw = draw
                    last_winner_board = boards[board_index]

                    # print(score(draw, boards[board_index]))
            
            #columns
            for i in range(5):
                count_col = 0
                for row in board:
                    if row[i] == 'X':
                        count_col += 1
                if count_col == 5 and board_index not in winners:
                    winners.append(board_index)
                    print("number drawn: " + str(draw))
                    print("board " + str(board_index + 1) + " has vertical bingo")

                    last_winner_draw = draw
                    last_winner_board = boards[board_index]

                    # print(score(draw, boards[board_index]))
            
            #diagonal
            # count_diag = 0
            # for i in range(5):
            #     if board[i][i] == 'X':
            #         count_diag += 1
            # if count_diag == 5:
            #     print("number drawn: " + str(draw))
            #     print("board " + str(board_index + 1) + " has diagonal bingo")
            #     print(board)

            #     print(score(draw, boards[board_index]))
            #     exit()
            
            # count_diag = 0
            # for i in range(5):
            #     if board[i][4 - i] == 'X':
            #         count_diag += 1
            # if count_diag == 5:
            #     print("number drawn: " + str(draw))
            #     print("board " + str(board_index + 1) + " has diagonal bingo")
            #     print(board)

            #     print(score(draw, boards[board_index]))
            #     exit()

    # print(last_winner_board)
    # print(last_winner_draw)

    print(score(last_winner_draw, last_winner_board))
    

def score(draw, board):
    draw = int(draw)
    non_x_sum = 0

    for row in board:
        for coord in row:
            if coord != 'X':
                non_x_sum += int(coord)
    
    return(draw * non_x_sum)


if __name__ == "__main__":
    main()