oedges = [map(int, x.split(' ')) for x in open('edges.txt', 'r').read().split('\n')[1:-1]]
vertices = set()
for edge in edges:
    vertices.add(edge[0])
    vertices.add(edge[1])
spanned = set()
spanned.add(vertices.pop())

total_cost = 0
while len(vertices)>0:
    best_cost = 9999999
    for edge in edges:
        if edge[0] in spanned and edge[1] in vertices and edge[2]<best_cost:
            best_cost = edge[2]
            best_vert = edge[1]
        if edge[1] in spanned and edge[0] in vertices and edge[2]<best_cost:
            best_cost = edge[2]
            best_vert = edge[0]
    spanned.add(best_vert)
    vertices.remove(best_vert)
    total_cost+=best_cost
print total_cost
