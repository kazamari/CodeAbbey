'''
You are given an array of values to sort. Implement the described algorithm and at each pass print out how many elements
of the array were shifted.

Input data will contain N - the size of array - in the first line. Next line will contain the array itself (all elements
will be different).
Answer should contain N-1 values showing how much elements are shifted at each pass.

Example:

input data:
4
3 1 2 5

answer:
1 1 0
'''


def insertion_sort(array):
    shifted = []
    for i in range(1, len(array)):
        tmp = array[i]
        k, s = i, 0
        while k > 0 and tmp < array[k - 1]:
            array[k] = array[k - 1]
            k -= 1
            s += 1
        array[k] = tmp
        shifted.append(s)
    return shifted


n = int(input())
print(*insertion_sort(list(map(int, input().split()))))
