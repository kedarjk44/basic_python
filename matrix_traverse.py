def print_spiral(last_row, last_column, matrix):
    start_row = 0
    start_column = 0
    while start_row < last_row and start_column < last_column:
        for i in range(start_column, last_column):
            print(matrix[start_row][i], end="kk ")

        start_row += 1
        for i in range(start_row, last_row):
            print(matrix[i][last_column - 1], end="ll ")
        last_column -= 1

        if start_row < last_row:
            for i in range(last_column-1, start_column-1, -1):
                print(matrix[last_row-1][i], end="mm ")
            last_row -= 1

        if start_column < last_column:
            for i in range(last_row - 1, start_row - 1, -1):
                print(matrix[i][start_column], end="nn ")
            start_column += 1


inp_matrix = [[1, 2, 3, "a"], [4, 5, 6, "b"], [7, 8, 9, "c"], [10, 11, 12, "d"]]
print_spiral(4, 4, inp_matrix)
