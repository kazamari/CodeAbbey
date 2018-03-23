'''
You will be given a fragment of text consisting of letters, spaces, punctuations and probably digits. You are to create the code-table by the rules above.

Input data will contain the text in a single line.
Answer should contain the pairs of ASCII-values and corresponding bit-strings of Shannon-Fano coding. Please output ASCII as decimals while bit-strings using letters O and I instead of digits 0 and 1 to help us determine possible mistakes easier. Also output the results in the same order as the letters were sorted during the algorithm.

Example:

input data:
ABRACADABRA

answer:
65 O 66 IO 82 IIO 67 IIIO 68 IIII
'''


def shannon_fano_encoder(s):
    def split_s(freq_table):
        min_diff, split_index = sum([w for x, w in freq_table]), 0
        for i in range(1, len(freq_table) + 1):
            diff = abs(sum([w for x, w in freq_table[:i]]) - sum([w for x, w in freq_table[i:]]))
            if diff < min_diff:
                min_diff = diff
            else:
                split_index = i - 1
                break
        return freq_table[:split_index], freq_table[split_index:]

    def code_table(fr_table):
        if len(fr_table) > 1:
            L, R = split_s(fr_table)
            for k, v in L:
                code[k] += '0'
            for k, v in R:
                code[k] += '1'
            code_table(L)
            code_table(R)

    fr_table = sorted({x: s.count(x) for x in s}.items(), key=lambda x: (-x[1], x[0]))
    code = {k: '' for k, v in fr_table}
    code_table(fr_table)
    return ' '.join([' '.join((str(ord(k)), v.replace('0', 'O').replace('1', 'I'))) for k, v in code.items()])


s = input()
print(shannon_fano_encoder(s))

