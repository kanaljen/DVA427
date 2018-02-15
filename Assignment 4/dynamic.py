from numpy import loadtxt


# Load dataset from file
dataset = loadtxt('city.txt', dtype='str', skiprows=3)

# Build node-dict
nodes = {}
for e in dataset:
    if e[0] not in nodes:
        nodes[e[0]] = 100
    elif e[1] not in nodes:
        nodes[e[1]] = 100
    else:
        continue

# Build edge-dict
edges = {}
for e in dataset:
    c = e[1] + e[0]
    edges[c] = int(e[2])

# Set source node
src = 'F'
nodes[src] = 0

iter = 0
edited = 1
# Bellman ford
for i in range(len(nodes) - 1):
    if edited == 0:
        break
    else:
        edited = 0
    # Loop nodes
    for v in nodes:
        # Loop edges
        for u in edges:
            iter += 1
            # If node v in edge u
            if v in u:
                w = edges[u]
                u = u.replace(v, "")
                if nodes[v] > nodes[u] + w:
                    nodes[v] = nodes[u] + w
                    edited = 1
            # If v not in u
            else:
                continue

print('Iterations:', iter)

print('V', 'D')
print('---')
for v in nodes:
    print(v, nodes[v])
