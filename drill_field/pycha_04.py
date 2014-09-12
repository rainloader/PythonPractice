def pycha_04(string):
    i = 0
    j = 0
    width = 80
    matrix = []
    row = [0 for col in range(width)]
    for char in string:
        row[i] = char
        i += 1
        if i >= 80:
            i = 0
            matrix.append(row)
            j += 1
            row = [0 for col in range(width)]
    height = j+1
    for ro in range(height):
        matrix2 = []
        for co in range(width):
            matrix2.append(matrix[ro][co])
        print(matrix2)
    
