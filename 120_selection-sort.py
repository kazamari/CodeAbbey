'''
Let us work in the following manner:

    - over the whole array find the position of the maximum element (5 in the case above - 0-based index of value 9);
    - swap this element with the last one (because in the sorted array it should be the last, of course) - i.e. with
    position N-1;
    - now regard the sub-array of length N-1, without the last value (which is already "in right place");
    - find the position of maximum element in this sub-array (i.e. second to maximum in the whole array) - now it would
    be index 7 (where the value 6 resides);
    - swap it with the last element in the sub-array (i.e. with position N-2);
    - now regard the sub-array of the length N-2 (without two last elements) - do the following selection and swap and
    so on;
    - algorithm ends when "sub-array" decreases to the length of 1.

Let us see an example step by step:

[3, 1, 4, 1, 5, 9, 2, 6, 5, 3]      - max is 9 at position 5, swap 5-th with 9-th
[3, 1, 4, 1, 5, 3, 2, 6, 5], 9      - max is 6 at position 7, swap 7-th with 8-th
[3, 1, 4, 1, 5, 3, 2, 5], 6, 9      - max is 5 at position 4, swap 4-th with 7-th - they are equal!
[3, 1, 4, 1, 5, 3, 2], 5, 6, 9      - max is 5 at position 4, swap 4-th with 6-th
[3, 1, 4, 1, 2, 3], 5, 5, 6, 9      - max is 4 at position 2, swap 2-th with 5-th
[3, 1, 3, 1, 2], 4, 5, 5, 6, 9
...
[1], 1, 2, 3, 3, 4, 5, 5, 6, 9      - subarray of length 1 is reached, stop an algorithm.

You are to implement the algorithm described above and print out the index of selected maximum at each pass.

Input data will contain N - the size of array - in the first line.
Next line will contain the array itself (all elements will be different).
Answer should contain indices of the maximums at each pass (N-1 values).

Example:

input data:
6
31 41 59 26 53 58

answer:
2 2 2 1 0
'''

def select_sort(array):
    indexes = []
    for i in reversed(range(1, len(array))):
        max_idx = i
        for j in reversed(range(i)):
            if array[max_idx] < array[j]:
                max_idx = j
        indexes.append(max_idx)
        array[i], array[max_idx] = array[max_idx], array[i]
    return indexes


n = int(input())
print(*select_sort(list(map(int, input().split()))))
