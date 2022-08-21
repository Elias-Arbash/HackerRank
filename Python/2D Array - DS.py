l = [[1, 1, 1, 0, 0, 0],
     [0, 1, 0, 0, 0, 0],
     [1, 1, 1, 0, 0, 0],
     [0, 0, 2, 4, 4, 0],
     [0, 0, 0, 2, 0, 0],
     [0, 0, 1, 2, 4, 0]]

r,c = len(l),len(l[0])

def hourglassSum(arr):
    x = 0
    h = []
    r,c = len(arr),len(arr[0])
    for i in range(r):
        for j in range(c):
            if (i >r-3) or (j>c-3):
                break
            else:
                x = l[i][j] + l[i][j+1] + l[i][j+2] \
                           + l[i+1][j+1] \
                   +l[i+2][j] + l[i+2][j+1] + l[i+2][j+2]
                h.append(x)
    
    return max(h)


print(hourglassSum(l))
