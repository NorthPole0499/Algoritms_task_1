def transp(data):
    new_matrix = []
    elem_of_new_matr = []
    for i in range(len(data[0])):
        for j in range(len(data)):
            elem_of_new_matr.append(data[j][i])
        new_matrix.append(elem_of_new_matr)
        elem_of_new_matr = []
    return new_matrix


def multiplication(first_matrix):
    print("Введите матрицу, на которую хотите умножить, построчно. "
          "Когда вы закончите вводить данные, нажмите дважды клавишу Enter")
    second_matrix = []
    while True:
        elem = input()
        if elem == '':
            break
        else:
            second_matrix.append(list(map(int, elem.split())))
    second_matrix = transp(second_matrix)

    new_matrix = []
    elem_of_new_matrix = []
    value = 0
    for i in range(len(first_matrix)):
        for j in range(len(second_matrix)):
            for k in range(len(first_matrix[i])):
                value += first_matrix[i][k] * second_matrix[j][k]
            elem_of_new_matrix.append(value)
            value = 0
        new_matrix.append(elem_of_new_matrix)
        elem_of_new_matrix = []
    return new_matrix



matrix = []
print("Введите матрицу построчно. Когда вы закончите вводить данные, нажмите дважды клавишу Enter")
while True:
    elem = input()
    if elem == '':
        break
    else:
        matrix.append(list(map(int, elem.split())))
print(multiplication(matrix))
