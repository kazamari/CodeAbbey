def lcg(a, c, modulus, seed, n):
    while True:
        seed = (a * seed + c) % modulus
        yield seed % n + 1

n, x0 = 10, 0

gen = lcg(445, 700001, 2097152, x0, n)
graph = {}
# print([x % n + 1 for _, x in zip(range(n), gen)])
#
for i in range(n):
    V1, D1, V2, D2 = next(gen), next(gen), next(gen), next(gen)
    graph.update({i+1: [(V1, D1), (V2, D2)]})
    for k, v in graph:
        if i in [x[0] for x in v]:
            graph[i].append((k, ))


print(graph)

# a,c,m,n,x0=[445, 700001, 2097152]+[10, 0]
# graph=[]
# for i in range(n): graph.append(dict())
# verts=[]
# for i in range(n*4):
#     x0=(a*x0+c)%m
#     verts.append(x0%n)
# print(verts)
# print(verts[0::4],verts[1::4],verts[2::4],verts[3::4])
#
# verts=zip(verts[0::4],verts[1::4],verts[2::4],verts[3::4])
#
# print(verts)
#
# for i,v in enumerate(verts):
#     print(i, v)
#     if v[0] not in graph[i] and v[0] != i:
#         graph[i][v[0]]=v[1]+1
#         graph[v[0]][i]=v[1]+1
#     if v[2] not in graph[i] and v[2] != i:
#         graph[i][v[2]]=v[3]+1
#         graph[v[2]][i]=v[3]+1
#
# print(graph)

# for i in range(n):
#     print(sum(graph[i][x] for x in graph[i]))