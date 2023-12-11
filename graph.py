'''vertex and edge
directed and undirected
weighted graphs- each edge has a weight associated w it
trees are a special case of a graph

Adjacency matrix
- symmetric for bidirectional graph
- each vertex has to store all of the vertices it is not connected to
- thus space complexity- O(V^2) #V is the number of vertices
- not ideal when the data we have is large
- adding vertex- we need to add a new row and column- have to rewrite entire matrix - O(V^2)
- adding edge- simple modification- O(1)
- removing edge- simple modification- O(1)
- removing vertex- have to rewrite entire matrix- O(V^2)

Adjacency list
- a dictionary- key is a vertex, value is list of vertices that the key has an edge with
- only stores the edges present for each vertex
- space complexity- O(V+E) #E is number of edges present
- adding vertex- simply add a key value pair to dictionary -O(1)
- adding edge- simple modification- O(1)
- removing edge- we need to iterate through the vertices' list of edges and remove- O(E)
- remove vertex- remove the key value pair for the vertex AND iterate throught the other vertices to find if there is an edge preset- O(V+E) 
'''

#Non weighted graph, bidirectional, adjacency list implementation
class Graph:
    def __init__(self):
        self.adj_list={}
    
    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex,":",self.adj_list[vertex])

    def add_vertex(self,vertex):
        if vertex not in self.adj_list.keys(): #check if vertex is not already in list
            self.adj_list[vertex]=[]
            return True
        return False

    def add_edge(self,v1,v2): 
        #check if v1 and v2 are present in the adj list- valid vertices
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self,v1,v2):
        #check if the vertices are valid and if the edge exists
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

    def remove_vertex(self,vertex):
        #we need to first remove all the edges to the vertex then remove the vertex
        #traverse through the vertex's list and go to the correspodning vertex and remove edge. more efficient
        if vertex in self.adj_list.keys(): #vertex exists
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False


graph=Graph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")

graph.add_edge("A","B")
graph.add_edge("A","C")
graph.add_edge("A","D")
graph.add_edge("B","D")
graph.add_edge("C","D")
graph.print_graph()

print()
graph.remove_vertex("D")

graph.print_graph()