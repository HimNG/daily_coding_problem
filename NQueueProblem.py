N = 6


def isSafe(arr, row, col):
    for i in range(N):
        if ((arr[i][col] == 1 and i != row) or (arr[row][i] == 1 and i != col)):
            return False

    diag1 = row-col
    diag2 = row+col

    for i in range(N):
        for j in range(N):
            diff1 = i-j
            diff2 = i+j
            if((diff1 == diag1 or diff2 == diag2) and (i != row) and (j != col) and (arr[i][j] == 1)):
                return False

    return True


def NqueueProblemUtil(arr, r):
    if r == N:
        return True

    for i in range(N):
        if(isSafe(arr, r, i)):
            arr[r][i] = 1
            if NqueueProblemUtil(arr, r+1):
                return True

            arr[r][i] = 0

    return False


def NqueueProblem():
    # arr = [[0] * N] * N   # dangerous to create 2D array like this.
    arr = [[0 for i in range(N)] for j in range(N)]
    # print(arr)
    if not NqueueProblemUtil(arr, 0):
        print("no answer")
        return False

    # print(arr)
    for row in arr:
        print(row)
    return True


if __name__ == '__main__':
    NqueueProblem()
