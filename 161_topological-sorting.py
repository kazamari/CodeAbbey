'''
Input data will contain the amount of discovery code pairs in the first line.
Next lines will contain two discovery codes each - so that first is required to start working on the second.
Answer should give a list of codes ordered according to topological sorting. (any such ordering is acceptable if there
are more than one)

Example:

input data:
5
Wr Mm
Mm Na
As Na
Na Py
Py Se

answer:
Wr As Mm Na Py Se
'''
from sys import stdin


def toposort(graph):
    sorted_list = []
    roots = set([x for x, y in graph]) - set([y for x, y in graph])

    while len(roots) != 0:
        node_from = roots.pop()
        sorted_list.append(node_from)
        for edge in [e for e in graph if e[0] == node_from]:
            node_to = edge[1]
            graph.remove(edge)
            if len([e for e in graph if e[1] == node_to]) == 0:
                roots.add(node_to)

    return sorted_list


graph = [(x, y) for x, y in [line.rstrip().split() for i, line in enumerate(stdin) if i > 0]]
print(*toposort(graph))