import numpy as np


# Load dataset from file
dataset = np.loadtxt('city.txt', dtype='str', skiprows=3)

# Build vertex dict
vertex = {}
for e in dataset:
    if e[0] not in vertex:
        vertex[e[0]] = 100
    elif e[1] not in vertex:
        vertex[e[1]] = 100
    else:
        continue

# Build distance dict
dist = {}
for e in dataset:
    c = e[1] + e[0]
    dist[c] = int(e[2])

# Set source vertex
src = 'F'
vertex[src] = 0

iter = 0
# Bellman ford
for i in range(len(vertex)-1):
    for v in vertex:
        for u in dist:
            if v in u:
                w = dist[u]
                iter += 1
                u = u.replace(v, "")
                if vertex[v] > vertex[u] + w:
                    vertex[v] = vertex[u] + w
            else:
                continue


print('Iterations:',iter)

print('V', 'D')
print('---')
for v in vertex:
    print(v, vertex[v])
