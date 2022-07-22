def is_isolate(arr, x, y):
    n = len(arr)
    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0 <= x + i < n and 0 <= y + j < n:
                if (i or j) and arr[x + i][y + j]:
                    return False
    return True
 
 
def verify(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1 and not is_isolate(arr, i, j):
                return False
    return True
 
 
a = [[1, 0, 0, 0, 0],
     [0, 0, 1, 0, 1],
     [0, 0, 0, 0, 0],
     [0, 1, 0, 1, 0],
     [0, 0, 0, 0, 0]]
print(verify(a))