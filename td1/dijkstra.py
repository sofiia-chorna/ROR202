import numpy as np
import graph
import priorityQueue

def dijkstra(g, startNode='a'):
    # Initialize priority queue, distances, and previous vertices
    queue = priorityQueue.PriorityQueue()
    distances = {node: float('inf') for node in g.nodes}
    distances[startNode] = 0
    previous_vertices = {node: None for node in g.nodes}

    # Insert all vertices into the priority queue
    for node, distance in distances.items():
        queue.insert((node, distance))

    # Main loop of Dijkstra's algorithm
    while not queue.isEmpty():
        min_vertex, min_distance = queue.extract_min()
        min_vertex_index = g.indexOf(min_vertex)

        # Iterate over edges to find neighbors of the extracted vertex
        for neighbor_index, weight in enumerate(g.adjacency[min_vertex_index]):
            # Check if there is an edge between the vertices
            if weight != 0:
                neighbor_vertex = g.nodes[neighbor_index]
                new_distance = min_distance + weight
                
                # The new distance is smaller than the current distance of the neighbor
                if new_distance < distances[neighbor_vertex]:
                    distances[neighbor_vertex] = new_distance
                    previous_vertices[neighbor_vertex] = min_vertex
                    queue.insert((neighbor_vertex, new_distance))

    return previous_vertices, distances

def main():
    # Créer un graphe contenant les sommets a, b, c, d, e, f, g 
    g = graph.Graph(np.array(["a", "b", "c", "d", "e", "f", "g"]))

    # Ajouter les arêtes
    g.addEdge("a", "b",  1.0)
    g.addEdge("a", "c",  3.0)
    g.addEdge("b", "c",  2.0)
    g.addEdge("b", "d",  5.0)
    g.addEdge("b", "e",  7.0)
    g.addEdge("b", "f",  9.0)
    g.addEdge("c", "d",  4.0)
    g.addEdge("d", "e",  6.0)
    g.addEdge("d", "g", 12.0)
    g.addEdge("e", "f",  8.0)
    g.addEdge("e", "g", 11.0)
    g.addEdge("f", "g", 10.0)
    
    # Run Dijkstra's algorithm
    previous_vertexes, distances = dijkstra(g)

    # Display the results
    print("Previous vertices:", previous_vertexes)
    print("Distances from start node:", distances)



if __name__ == '__main__':
    main()
