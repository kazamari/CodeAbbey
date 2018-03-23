'''
Let's write a program that sieves necessary words from the given text, and prints them in the proper order.

Input data consist of about 300 words, each made of 3 Latin letters. The end is signaled by the word end.
Answer should contain all the words which are encountered more than once in lexicographic order.

Example:

input data:
nun lam mip tex bal pif sot bal bod tex end

answer:
bal tex

Note: although for small amount of words one can write double nested loop to compare words, this approach is inefficient
for large numbers of words - it is not suitable for one million words etc. Try to invent a better approach.
'''

s, dict, i = input(), {}, 0

while i < len(s):
    word = s[i:i+3]
    if word in dict.keys():
        dict[word] += 1
    else:
        dict.update({word: 1})
    i = i + 4

print(*sorted([key for key, value in dict.items() if value > 1]))
