import numpy as np
import graph
import sys
import disjoinedSet

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
    
    # Obtenir un arbre couvrant de poids minimal du graphe
    tree = kruskal(g)
    
    # S'il existe un tel arbre (i.e., si le graphe est connexe)
    if tree != None:
        
        # L'afficher
        print(tree)

    else:
        print("Pas d'arbre couvrant")


# Applique l'algorithme de Kruskal pour trouver un arbre couvrant de poids minimal d'un graphe
# Retourne: Un arbre couvrant de poids minimal du graphe ou None s'il n'en existe pas
def kruskal(g):
    # Créer un nouveau graphe contenant les mêmes sommets que g
    tree = graph.Graph(g.nodes)
    
    # Récupérer toutes les arêtes de g
    edges = g.getEdges()
    
    # Trier les arêtes par poids croissant
    edges.sort(key=lambda x: x.weight)
    
    # Regarger quelles nodes sont déjà connectées
    connectedNodes = disjoinedSet.DisjointSet(len(g.nodes))

    for edge in edges:
        nodeA = g.nodes[edge.id1]
        nodeB = g.nodes[edge.id2]

        if connectedNodes.find(edge.id1) != connectedNodes.find(edge.id2):
            # Union des nodes
            print(f"'{nodeA}' - '{nodeB}' no cycle -> union")
            connectedNodes.union(edge.id1, edge.id2)
            
            # Ajouter à l'arbre
            tree.addEdge(nodeA, nodeB, edge.weight)
        else:
            print(f"'{nodeA}' - '{nodeB}' form cycle -> skipping")

    return tree


if __name__ == '__main__':
    main()
