

def _get_hourglass_sum(matrix, row, col):
    sum = 0
    sum += matrix[row-1][col-1]
    sum += matrix[row-1][col]
    sum += matrix[row-1][col+1]
    sum += matrix[row][col]
    sum += matrix[row+1][col-1]
    sum += matrix[row+1][col]
    sum += matrix[row+1][col+1]
    return sum



def solution(x):
    max_hourglass_sum = -63
    for i in range(1,5):
        for j in range(1,5):
            curren_hourglass_sum = _get_hourglass_sum(x,i,j)
            if curren_hourglass_sum > max_hourglass_sum:
                max_hourglass_sum = curren_hourglass_sum
    return max_hourglass_sum


if __name__ == '__main__':
    # arr = []
    # for _ in range(6):
    #     arr.append(list(map(int, input().rstrip().split())))
    arr_0 = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]
    print(solution(arr_0))