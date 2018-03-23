'''
Please implement the described algorithm and run it on a sample array. For each call of quicksort please output its
left and right parameters.

Input data will contain N - the size of array - in the first line.
Next line will contain the array itself (all elements will be different).
Answer should contain left-right ranges for each call of the recursive function in order. Separate values of each pair
with a dash, while pairs itself should be separated with spaces.

Example:

input data:
10
38 23 9 19 113 5 42 85 71 112

answer:
0-9 0-3 1-3 1-2 5-9 5-8 5-7
'''


def partition(array, left, right):
    lt, rt, dir, pivot = left, right, 'left', array[left]
    while lt < rt:
        if dir == 'left':
            if array[rt] > pivot:
                rt -= 1
            else:
                array[lt], dir = array[rt], 'right'
                lt += 1
        else:
            if array[lt] < pivot:
                lt += 1
            else:
                array[rt], dir = array[lt], 'left'
                rt -= 1
    array[lt] = pivot
    return lt


def quicksort(array, left, right):
    print('{}-{}'.format(left,right), end=' ')
    pivot_pos = partition(array, left, right)
    if pivot_pos - left > 1:
        quicksort(array, left, pivot_pos - 1)
    if right - pivot_pos > 1:
        quicksort(array, pivot_pos + 1, right)


n = int(input())
l = list(map(int, input().split()))
quicksort(l, 0, len(l)-1)
