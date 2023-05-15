"""
Write a program to print a matrix of 2-dimension Matrix in Spiral Order.
"""
max = [[1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]]


def fun(a):
    row = len(a[0])
    col = len(a)

    left = 0
    right = row-1
    top = 0
    bottom = col-1

    result = []

    while left <= right and top <= bottom:
        # Adding top row(remaining matrix) to the result.
        for i in range(left, right+1):
            result.append(a[top][i])
        top += 1

        # Adding last column(remaining matrix) to the result.
        for i in range(top, bottom+1):
            result.append(a[i][right])
        right -= 1

        # Adding last row(remaining matrix) to the result.
        if top <= bottom:
            for i in range(right, left-1, -1):
                result.append(a[bottom][i])
            bottom -= 1

        # Adding first column(remaining matrix) to the result.
        if left <= right:
            for i in range(bottom, top-1, -1):
                result.append(a[i][left])
            left += 1
    
    return result


print(fun(max))


"""
OUTPUT:
>>> [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
"""
