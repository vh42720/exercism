class Matrix:
    def __init__(self, matrix_string):
        # Initialize the empty list of row and column
        self.rows = [row.split() for row in matrix_string.splitlines()]
        self.rows = [list(map(int, row)) for row in self.rows]

        # Create list of columns based on rows
        self.columns = list(map(list, zip(*self.rows)))

    def row(self, index):
        return self.rows[index-1]

    def column(self, index):
        return self.columns[index-1]


m = Matrix(matrix_string='1 2 \n 10 20')
print(m.rows)
print(m.columns)
