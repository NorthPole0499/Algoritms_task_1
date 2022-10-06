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


def rank(matrix):
    minor_data = []
    a1, a2, a3 = matrix[0][0], matrix[1][0], matrix[2][0]
    b1, b2, b3 = matrix[0][1], matrix[1][1], matrix[2][1]
    c1, c2, c3 = matrix[0][2], matrix[1][2], matrix[2][2]
    new_a1 = c2 * b3 - b2 * c3
    new_a2 = c1 * b3 - b1 * c3
    new_a3 = c1 * b2 - b1 * c2
    new_b1 = c2 * a3 - a2 * c3
    new_b2 = c1 * a3 - a1 * c3
    new_b3 = c1 * a2 - a1 * c2
    new_c1 = b2 * a3 - a2 * b3
    new_c2 = b1 * a3 - a1 * b3
    new_c3 = b1 * a2 - a1 * b2
    main_minor = a1 * b2 * c3 + a2 * b3 * c1 + a3 * b1 * c2 - a3 * b2 * c1 - a2 * b1 * c3 - a1 * b3 * c2
    minor_data.append((new_a1, new_b1, new_c1, new_a2, new_b2, new_c2, new_a3, new_b3, new_c3))
    if max(minor_data[0]) == 0:
        max_minor = 1
    elif max(minor_data[0]) > main_minor:
        max_minor = 2
    else:
        max_minor = 3
    return max_minor


matrix = []
print("Введите матрицу построчно. Когда вы закончите вводить данные, нажмите дважды клавишу Enter")
while True:
    elem = input()
    if elem == '':
        break
    else:
        matrix.append(list(map(int, elem.split())))

print(transp(matrix))
print(rank(matrix))
print(multiplication(matrix))
