route = [('Cowsome', 'Honepy'), ('Bawnty', 'Cowsome'), ('Lacry', 'Bawnty'), ('Honepy', 'Maycorn'),
             ('Maycorn', 'Bawnty'), ('Mikliday', 'Cowsome'), ('Mausse', 'Lednec'), ('Maycorn', 'Mausse'),
             ('Bawnty', 'Mausse'), ('Mikliday', 'Maycorn'), ('Lednec', 'Maycorn')]

# def transitive_closure(elements):
#     elements = set([(x,y) if x < y else (y,x) for x,y in elements])
#
#     relations = {}
#     for x,y in elements:
#         if x not in relations:
#             relations[x] = []
#         relations[x].append(y)
#
#     closure = set()
#     def build_closure(n):
#         def f(k):
#             for y in relations.get(k, []):
#                 closure.add((n, y))
#                 f(y)
#         f(n)
#
#     for k in relations.keys():
#         build_closure(k)
#
#     return closure

def transitive_closure(array):
    new_list = [set(array.pop(0))]  # initialize first set with value of index `0`

    for item in array:
        for i, s in enumerate(new_list):
            if any(x in s for x in item):
                new_list[i] = new_list[i].union(item)
                break
        else:
            new_list.append(set(item))
    return new_list

def count_route(pair):
    new_list = set()
    for item in route:
        if any(x in pair for x in item):
            new_list.update(set(item))
    return new_list

# print(transitive_closure(route))

# print(count_route(('Cowsome', 'Mausse')))

new_list = set()
for item in route:
    if any(x in ('Cowsome', 'Mausse') for x in item):
        new_list.update(set(item))

print(new_list)