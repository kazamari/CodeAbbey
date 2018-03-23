'''
n this problem you should create such interpreter. Do not be afraid - it is easier to write Brainfuck interpreter itself
than to write Brainfuck problems for such interpreter.

We ask you to implement slightly altered version of the language - Brainfuck++ which includes two additional
commands ; and :.

Please, refer to the wiki article by the link above to read specification of the language.

Input data will contain two lines.
The first input line contains Brainfuck program without any spare characters.
The second line contains a sequence of numbers which would be consumed as input.
Answer should contain output of the program.

Example:

input data:
;>;<[->+<]:>:
3 5

answer:
0 8
'''

def bf_interpreter(prog, params):
    mem_size, res = 30000, []
    a = [0] * mem_size
    p, argi, i = 0, 0, 0

    while i < len(prog):
        s = prog[i]
        if s == '>':
            p = (p + 1) % mem_size
        elif s == '<':
            p = (p - 1) % mem_size
        elif s == '+':
            a[p] += 1
        elif s == '-':
            a[p] -= 1
        elif s == '.':
            res.append(chr(a[p]))
        elif s == ':':
            res.append(str(a[p]))
        elif s == ',':
            if argi < len(params):
                a[p] = ord(params[argi])
                argi += 1
            else:
                a[p] = 0
        elif s == ';':
            a[p] = params[argi]
            argi += 1
        elif s == '[':
            if a[p] == 0:
                loop = 1
                while loop > 0:
                    i += 1
                    if prog[i] == '[':
                        loop += 1
                    elif prog[i] == ']':
                        loop -= 1
        elif s == ']':
            loop = 1
            while loop > 0:
                i -= 1
                if prog[i] == '[':
                    loop -= 1
                elif prog[i] == ']':
                    loop += 1
            i -= 1
        i += 1

    return res

# s = '++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.'
# print(bf_interpreter(s, ''))
# s = '+++++:'
# print(bf_interpreter(s, ''))
# s = '+++++++++++++++++++++++++++++++++.'
# print(bf_interpreter(s, ''))
# s = '++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.'
# print(bf_interpreter(s, ''))
# s = ';>;[-<+>]<:'
# print(bf_interpreter(s, list(map(int, '3 5'.split()))))
# s = ';>;<[->+<]:>:'
# print(*list(bf_interpreter(s, list(map(int, '3 5'.split())))))
# s = ';>;<+++[>+<-]+:>-:<:+++[->++<][->+<];+:>-:<+++:[->+>+<<]>>[-<<+>>]<<>;<+++>:<[>+<-]>-<>-<:+:>-:<[->++<]>;<[->++<]+:>-:<[->+<]+++>-<[>+<-][>+<-][->+>+<<]>>[-<<+>>]<<>++++<[->+>+<<]>>[-<<+>>]<<[->+>+<<]>>[-<<+>>]<<>:<>:<:>:'
# print(*list(bf_interpreter(s, list(map(int, '10 11 19 15 7'.split())))))
# s = ';>;<;>++++<>;<[->++<][->+>+<<]>>[-<<+>>]<<>:<>++++<;>-<+:>-:<>-<[->++<]+:>-:<[>+<-];>-<[->+>+<<]>>[-<<+>>]<<>:<;[->+<][->++<][->+>++<<]>++++<>-<[>+<-]>:<[->++<][->+>++<<]>++++<>-<[>+<-][->+>++<<][->+>+<<]>>[-<<+>>]<<+++[>+<-]+++>++++<>-<>-<[>+<-]>-<>++++<[->++<][>+<-][->++<]+:>-:<>;<:;>;<;+:>-:<+:>-:<:>:'
# params = '16 14 15 15 14 15 6 18 11 11 17'
# res: 45 15 47 1 75 90 99 1 112 1 18 10 19 9 19 9
# s = ';>;<+++[->+<];[->+>+<<]>>[-<<+>>]<<[->++<]>++++<+:>-:<>++++<[->+>++<<]>;<[->+<][>+<-][->+<]+:>-:<[->++<][->++<];+:>-:<>-<>-<[->++<]+:>-:<[->+>++<<][>+<-]>;<>:<;:[->+<]+++>;<[->++<][>+<-]:[->+>++<<][->+>+<<]>>[-<<+>>]<<>-<::>:'
# params = '3 5 10 5 12 10 4 6'

# prog = input()
# params = list(map(int, input().split()))
#
# print(*bf_interpreter(prog, params))

# s = '++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.'
# # s = ',[.,]'
# # s = ',[>,]<[.<]'
# s = '>+>+>+>+>++<[>[<+++>-]<<]>.'
# params = 'VENI VIDI VICI'
# print(*bf_interpreter(s, params))

prog = input()
params = list(map(int, input().split()))

print(*bf_interpreter(prog, params))