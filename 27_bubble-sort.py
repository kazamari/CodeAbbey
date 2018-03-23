'''
We are going to implement the described version of Bubble-Sort. To test it we will check the amount of passes
and amount of swaps made before the given array becomes ordered.

Input data will contain array size in first line and array itself in the second (integer values separated with spaces).
Answer should contain two values - number of passes perfromed and total number of swaps made. For example:

input data:
8
3 1 4 1 5 9 2 6

answer:
5 8

We may note that number of swaps is roughly proportional to N^2 where N is array size (average is about N^2 / 4)
so that time which algorithm takes grows significantly faster than the amount of data (that is why such sorting
is rarely used for bigger arrays).
'''

def bubble_sort(list):
    x, sumn = 0, 0
    while True:
        n = 0
        for i in range(len(list) - 1):
            if list[i] > list[i+1]:
                    list[i], list[i+1] = list[i+1], list[i]
                    n += 1
        x += 1
        sumn += n
        if n == 0:
            break

    return [x, sumn]

m = int(input())
print(*bubble_sort(list(map(int, input().split()))))

