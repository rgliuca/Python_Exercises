def create_2D_list(num_rows, num_cols):
    return [[num_cols*row + col for col in range(num_cols)] for row in
            range(num_rows)]
