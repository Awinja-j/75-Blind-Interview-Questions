def flippingMatrix(matrix):
    n = len(matrix)
    d = 0

    for i in range(n + 1):
        for j in range(n + 1):
            f = matrix[i][j]
            s = matrix[n-i-1][j]
            a = matrix[i][n-j-1]
            z = matrix[n-i-1][n-j-1]
            print(f, s, a, z)
            d = max(matrix[i][j], matrix[i][n-j-1], matrix[n-i-1][j], matrix[n-i-1][n-j-1])
            # d += max(matrix[row][col], matrix[row][2*n-col-1], matrix[2*n-row-1][col], matrix[2*n-row-1][2*n-col-1])
    print(d)
    return d

# print(flippingMatrix([[1,2],[3,4]]))
print(flippingMatrix([[112,42, 83, 119],[56, 125, 56,49], [15, 78,101, 43], [62, 98, 114, 108]]))
