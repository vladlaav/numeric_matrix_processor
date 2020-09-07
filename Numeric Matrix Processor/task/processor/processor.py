from math import floor

def sum_matrs(matr1, matr2):
    if len(matr1) == len(matr2) and len(matr1[0]) == len(matr2[0]):
        row, col = len(matr1), len(matr1[0])
        matr_sum = []
        for i in range(row):
            matr_sum.append([])
            for j in range(col):
                matr_sum[i].append(matr1[i][j] + matr2[i][j])
        return matr_sum
    else:
        return None


def multiply_const(matr, const):
    const = float(const) if '.' in const else int(const)
    row, col = len(matr), len(matr[0])
    matr_res = []
    for i in range(row):
        matr_res.append([])
        for j in range(col):
            matr_res[i].append(const * matr[i][j])
    return matr_res


def multiply_matrs(matr1, matr2):
    if len(matr1[0]) == len(matr2):
        matr_res = []
        for i in range(len(matr1)):
            matr_res.append([])
            for j in range(len(matr2[0])):
                multi_res = 0
                for k in range(len(matr2)):
                    multi_res += matr1[i][k] * matr2[k][j]
                matr_res[i].append(multi_res)
        return matr_res
    else:
        return None


def add(number=''):
    print(f'Enter size of {number}matrix:', end='')
    row, col = [int(n) for n in input().split()]
    print(f'Enter {number}matrix:')
    matr = [[float(n) if '.' in n else int(n)
             for n in input().split()] for r in range(row)]
    return matr


def output(matr):
    print('The result is:')
    if matr is None:
        print('The operation cannot be performed.')
    else:
        for row in matr:
            for el in row:
                print(el, end=' ')
            print()


def transpose_main_d(matr):
    matr_res = [[0 for el in matr] for row in matr[0]]
    for row in range(len(matr)):
        for col in range(len(matr[0])):
            matr_res[col][row] = matr[row][col]
    return matr_res


def transpose_side_d(matr):
    matr_res = [[0 for el in matr] for row in matr[0]]
    for i in range(len(matr)):
        n = len(matr) - 1 - i
        for j in range(len(matr[0])):
            m = n - j
            matr_res[i + m][j + m] = matr[i][j]
    return matr_res


def traspose_vertical(matr):
    matr_res = [[0 for el in matr[0]] for row in matr]
    for row in range(len(matr)):
        n = len(matr[0]) - 1
        for col in range(len(matr[0])):
            matr_res[row][col + n] = matr[row][col]
            n -= 2
    return matr_res


def transpose_horizontal(matr):
    matr_res = [[0 for el in matr[0]] for row in matr]
    for col in range(len(matr)):
        n = len(matr) - 1
        for row in range(len(matr[0])):
            matr_res[row + n][col] = matr[row][col]
            n -= 2
    return matr_res


def determinant_calc(matr):
    if len(matr) == 1:
        return matr[0][0]
    elif len(matr) == 2:
        return matr[0][0] * matr[1][1] - matr[0][1] * matr[1][0]
    elif len(matr) > 2:
        return sum(pow(-1, 0 + j) * matr[0][j] * determinant_calc(minor(matr, 0, j))
                   for j in range(len(matr)))


def minor(matr, row, col):
    matr_res = []
    r_res = 0
    for r in range(len(matr)):
        if r != row:
            matr_res.append([])
        for c in range(len(matr)):
            if r != row and c != col:
                matr_res[r_res].append(matr[r][c])
        if r != row:
            r_res += 1
    return matr_res


def inverse_matr(matr):
    matr_res = []
    det_matr = determinant_calc(matr)
    if det_matr == 0:
        return False
    else:
        for row in range(len(matr)):
            matr_res.append([])
            for col in range(len(matr[0])):
                matr_res[row].append(pow(-1, row + col) * determinant_calc(minor(matr, row, col)))
        return multiply_const(transpose_main_d(matr_res), str(1 / det_matr))


def menu():
    while True:
        act = int(input('''1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit
Your choice: '''))
        if act == 1:
            output(sum_matrs(add('first '), add('second ')))
        elif act == 2:
            output(multiply_const(add(), input('Enter constant:')))
        elif act == 3:
            output(multiply_matrs(add('first '), add('second ')))
        elif act == 4:
            act = int(input('''1. Main diagonal
            2. Side diagonal
            3. Vertical line
            4. Horizontal line
            Your choice:'''))
            if act == 1:
                output(transpose_main_d(add()))
            elif act == 2:
                output(transpose_side_d(add()))
            elif act == 3:
                output(traspose_vertical(add()))
            elif act == 4:
                output(transpose_horizontal(add()))
        elif act == 5:
            print('The result is:\n', determinant_calc(add()))
        elif act == 6:
            inverse_matrix = inverse_matr(add())
            if inverse_matrix:
                output(inverse_matrix)
            else:
                print('This matrix doesn\'t have an inverse.\n')
        elif act == 0:
            break


if __name__ == '__main__':
    menu()
