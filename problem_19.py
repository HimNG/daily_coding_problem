'''
A builder is looking to build a row of N houses that can be of K different colors.
He has a goal of minimizing cost while ensuring that no two neighboring houses are
of the same color.
Given an N by K matrix where the nth row and kth column represents the cost to build
the nth house with kth color, return the minimum cost which achieves this goal.
max price = 1000
'''

import copy
import sys
# NumberOfTestCases = int(input())
NumberOfColors = int(input())

# for i in range(NumberOfTestCases):

NumberOfHouses = int(input())
colorprice = [[sys.maxsize for i in range(
    NumberOfColors)] for j in range(NumberOfHouses)]
for j in range(NumberOfHouses):
    input_string = input()
    li = input_string.split()
    k = 0
    for num in li:
        colorprice[j][k] = int(num)
        k = k+1

prev_index = -1
sum = 0
for house in range(NumberOfHouses):
    min_ele = min(colorprice[house])
    min_index = colorprice[house].index(min_ele)
    # print("min_el")
    if min_index == prev_index:
        l_temp = copy.deepcopy(colorprice[house])
        del l_temp[min_index]
        min_ele = min(l_temp)
        min_index = colorprice[house].index(min_ele)

    print("min_ele=", min_ele)
    sum = sum + int(min_ele)

    prev_index = min_index

print(sum)
