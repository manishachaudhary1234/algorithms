edges = [map(int, x.split(' ')) for x in open('clustering1.txt', 'r').read().split('\n')[1:-1]]

edges.sort(key=lambda x: x[2])

vertices = {}
for edge in edges:
    vertices[edge[0]] = edge[0]
    vertices[edge[1]] = edge[1]

costs = {}
for v in vertices:
    costs[v] = 0

cluster_count = len(vertices)

for edge in edges:
    head1 = vertices[edge[0]]
    while vertices[head1] != head1:
        head1 = vertices[head1] 

    head2 = vertices[edge[1]]
    while vertices[head2] != head2:
        head2 = vertices[head2] 

    if head1 != head2:
        if cluster_count <= 4:
            spacing_distance = edge[2]
            break
        vertices[head2] = head1
        costs[head1] += (edge[2] + costs[head2])
        cluster_count -= 1

print spacing_distance
