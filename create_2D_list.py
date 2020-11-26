def create_2D_list(num_rows, num_cols):
    return [[num_cols*row + col for col in range(num_cols)] for row in
            range(num_rows)]


matrix = create_2D_list(10, 10)
for each_row in matrix:
    print(each_row)
