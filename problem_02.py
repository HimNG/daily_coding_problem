'''
Given an array of integers, return a new array such that each element at index i of the new array is the product of
all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was
[3, 2, 1], the expected output would be [2, 3, 6].

'''
import math


# with Division
def OutputArrayFunwithDivision(inputArray):

    totalProduct = 1
    OutputArray = []
    for i in inputArray:
        totalProduct *= i

    for i in inputArray:
        OutputArray.append(totalProduct//i)

    return OutputArray


# Using without Division
def OutputArrayFunwithoutDivision(inputArray):
    '''
    x=a*b*c
    log(x)=log(a)+log(b)+log(c)
    x=pow(10,(log(a)+log(b)+log(c)))
    '''

    sum = 0
    OutputArray = []
    n = len(inputArray)
    for i in range(n):
        sum += math.log10(inputArray[i])

    for i in range(n):
        num = round(pow(10.0, sum - math.log10(inputArray[i])))
        OutputArray.append(num)

    return OutputArray


if __name__ == '__main__':
    inputArray = [1, 2, 3, 4, 5]
    outputArraywithDivision = OutputArrayFunwithDivision(inputArray)
    print("With Division :", outputArraywithDivision)
    outputArraywithoutDivision = OutputArrayFunwithoutDivision(inputArray)
    print("Without Division :", outputArraywithoutDivision)
