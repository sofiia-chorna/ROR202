import numpy as np
import graph
from collections import deque


def main():
    # Le poids des arcs de ce graphe correspondent aux capacites
    g = example()

    # Le poids des arcs de ce graphe correspondent au flot
    flow = ford_fulkerson(g, "s", "t")

    print("Result :")
    print(flow)


# Fonction creant un graphe sur lequel sera applique l'algorithme de Ford-Fulkerson
def example():
    g = graph.Graph(np.array(["s", "a", "b", "c", "d", "e", "t"]))

    g.addArc("s", "a", 8)
    g.addArc("s", "c", 4)
    g.addArc("s", "e", 6)
    g.addArc("a", "b", 10)
    g.addArc("a", "d", 4)
    g.addArc("b", "t", 8)
    g.addArc("c", "b", 2)
    g.addArc("c", "d", 1)
    g.addArc("d", "t", 6)
    g.addArc("e", "b", 4)
    g.addArc("e", "t", 2)

    return g


# Fonction appliquant l'algorithme de Ford-Fulkerson a un graphe
# Les noms des sommets sources est puits sont fournis en entree
def ford_fulkerson(g, sName, tName):
    # Recuperer l'indice de la source et du puits
    s = g.indexOf(sName)
    t = g.indexOf(tName)

    # Create a new graph to store the flow
    flow = graph.Graph(g.nodes)

    # There exists a path from s to t in the residual graph
    while True:
        # Find a path from s to t in the residual graph
        path, min_residual_capacity = find_path(g, s, t, flow)
        if path is None:
            break

        # Update the flow along the path
        for u, v in path:
            flow.addArcByIndex(u, v, min_residual_capacity)
            flow.addArcByIndex(v, u, -min_residual_capacity)

    return flow


def find_path(g, s, t, flow):
    visited = [False] * len(g.nodes)
    queue = deque()

    # Initialize parent array to store the parent of each node in the path
    parent = [-1] * len(g.nodes)
    min_residual_capacity = float('inf')

    # Mark the source node as visited
    queue.append(s)
    visited[s] = True

    # BFS
    while queue:
        u = queue.popleft()

        for v in range(len(g.nodes)):
            if not visited[v] and (g.adjacency[u][v] - flow.adjacency[u][v] > 0):
                visited[v] = True
                parent[v] = u
                queue.append(v)

                # Reached the sink t -> break the loop
                if v == t:
                    break

    if visited[t]:
        v = t
        while parent[v] != -1:
            u = parent[v]
            min_residual_capacity = min(min_residual_capacity, g.adjacency[u][v] - flow.adjacency[u][v])
            v = u

        # Backtrack to construct the augmenting path
        v = t
        augmenting_path = []
        while parent[v] != -1:
            u = parent[v]
            augmenting_path.append((u, v))
            v = u

        # Reverse the augmenting path to get the correct order
        augmenting_path.reverse()
        return augmenting_path, min_residual_capacity

    # No augmenting path is found -> return None
    return None, 0


if __name__ == '__main__':
    main()
