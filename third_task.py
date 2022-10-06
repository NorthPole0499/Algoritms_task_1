import numpy


def rank_numpy(matrix):
    martix_rank = numpy.linalg.matrix_rank(matrix)
    return martix_rank


def transp_numpy(matrix):
    tr_matrix = numpy.transpose(matrix)
    return tr_matrix


def multiplication_numpy(first_matrix):
    second_matrix = []
    print("Введите матрицу построчно. Когда вы закончите вводить данные, "
          "нажмите дважды клавишу Enter")
    while True:
        elem = input()
        if elem == '':
            break
        else:
            second_matrix.append(list(map(int, elem.split())))
    second_matrix = numpy.array(second_matrix)
    answer = numpy.dot(first_matrix, second_matrix)
    return answer


matrix = []
print("Введите матрицу построчно. Когда вы закончите вводить данные, нажмите дважды клавишу Enter")
while True:
    elem = input()
    if elem == '':
        break
    else:
        matrix.append(list(map(int, elem.split())))
matrix = numpy.array(matrix)

print(transp_numpy(matrix))
print(rank_numpy(matrix))
print(multiplication_numpy(matrix))



