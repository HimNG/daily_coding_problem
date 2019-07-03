'''Given an array of integers, find the first missing positive integer in linear time and constant space. 
In other words, find the lowest positive integer that does not exist in the array. The array can contain 
duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.

'''


def FirstMissingPositiveInterger(inputArray):
    n = len(inputArray)

    for i in range(n):
        if inputArray[i] < 1 or inputArray[i] > n or inputArray[inputArray[i]-1] == inputArray[i]:
            pass
        else:
            j, temp = i, 1
            while temp != 0:
                if temp < i or inputArray[inputArray[j] - 1] < 1 or inputArray[inputArray[j] - 1] > n or inputArray[inputArray[i]-1] == inputArray[i]:
                    inputArray[inputArray[j]-1] = inputArray[j]
                    j = inputArray[j]-1
                    temp = 0
                else:
                    temp = inputArray[inputArray[j]-1]
                    inputArray[inputArray[j]-1] = inputArray[j]
                    j = inputArray[j]-1

    print(inputArray)


if __name__ == '__main__':
    inputArray = [3, 4, -1, 1]
    FirstMissingPositiveInterger(inputArray)
