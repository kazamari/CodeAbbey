from itertools import islice

def window_with_larger_step(fseq, window_size):
    """Sliding window

    The step size the window moves over increases with the size of the window.
    """
    it = iter(fseq)
    result = list(islice(it, 0, window_size))
    if len(result) == window_size:
        yield result
    step_size = max(1, int(round(window_size / 4)))  # no smaller than 1
    while True:
        new_elements = list(islice(it, step_size))
        if len(new_elements) < step_size:
            break
        result = result[step_size:] + list(islice(it, step_size))
        yield result

def window(seq, n=4096):
    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result

seq = '''in the town where i was born lived a man who sailed to sea
and he told us of his life in a land of submarines'''

for x in window(seq, 4):
    print(''.join(x))