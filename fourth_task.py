import numpy
import timeit

def transp(data):
    new_matrix = []
    elem_of_new_matr = []
    for i in range(len(data[0])):
        for j in range(len(data)):
            elem_of_new_matr.append(data[j][i])
        new_matrix.append(elem_of_new_matr)
        elem_of_new_matr = []
    return new_matrix



def minor(matrix):
    minor_matrix = []
    a1, a2, a3 = matrix[0][0], matrix[1][0], matrix[2][0]
    b1, b2, b3 = matrix[0][1], matrix[1][1], matrix[2][1]
    c1, c2, c3 = matrix[0][2], matrix[1][2], matrix[2][2]
    new_a1 = b2 * c3 - c2 * b3
    new_a2 = -1 * (b1 * c3 - c1 * b3)
    new_a3 = b1 * c2 - c1 * b2
    new_b1 = -1 * (a2 * c3 - c2 * a3)
    new_b2 = a1 * c3 - c1 * a3
    new_b3 = -1 * (a1 * c2 - c1 * a2)
    new_c1 = a2 * b3 - b2 * a3
    new_c2 = -1 * (a1 * b3 - b1 * a3)
    new_c3 = a1 * b2 - b1 * a2
    minor_matrix.append([new_a1, new_b1, new_c1])
    minor_matrix.append([new_a2, new_b2, new_c2])
    minor_matrix.append([new_a3, new_b3, new_c3])
    return minor_matrix


def opredelitel(matrix):
    a1, a2, a3 = matrix[0][0], matrix[1][0], matrix[2][0]
    b1, b2, b3 = matrix[0][1], matrix[1][1], matrix[2][1]
    c1, c2, c3 = matrix[0][2], matrix[1][2], matrix[2][2]
    opred = a1 * b2 * c3 + a3 * b1 * c2 + a2 * b3 * c1 - a3 * b2 * c1 - a1 * b3 * c2 - a2 * b1 * c3
    return opred


def reverse_matrix(matrix):
    opred = opredelitel(matrix)
    if opred == 0:
        return None
    else:
        matrix_alg_dop = minor(matrix)
        tr_matrix_alg_dop = transp(matrix_alg_dop)
        reverse_opred = 1 / opred
        answer = tr_matrix_alg_dop
        for i in range(len(tr_matrix_alg_dop)):
            for j in range(len(tr_matrix_alg_dop[i])):
                answer[i][j] = reverse_opred * tr_matrix_alg_dop[i][j]
        return answer


def reverse_matrix_numpy(matrix):
    num_matrix = numpy.array(matrix)
    answer = numpy.linalg.inv(num_matrix)
    return answer


matrix = []
print("Введите матрицу построчно. Когда вы закончите вводить данные, нажмите дважды клавишу Enter")
while True:
    elem = input()
    if elem == '':
        break
    else:
        matrix.append(list(map(int, elem.split())))


start_time = timeit.default_timer()
reverse_matrix(matrix)
a = '{:0.19f}'.format(timeit.default_timer() - start_time)
print(a)

start_time = timeit.default_timer()
reverse_matrix_numpy(matrix)
b = timeit.default_timer() - start_time
print(b)
print(b / float(a))




