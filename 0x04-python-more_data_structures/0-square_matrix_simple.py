#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    pass


def square_matrix_simple(matrix=[]):
    def row(line=[]):
        output = []
        for item in line:
            output.append(item ** 2)
        return (output)
    return list(map(row, matrix))
