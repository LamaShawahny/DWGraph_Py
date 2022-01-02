# Directed Weighted Graph

### Task :

Design and implement an Directed Weighted graph or in other words Assigment 2  in PYTHON .

![OOP IMG](https://user-images.githubusercontent.com/74476764/147874740-29a6c7aa-fe2a-42b9-a87f-47ffd90250ab.jpeg)
                        Photoge of a graph that we created using Plot function .

### Design:
- This class represents a directed weighted graph
that can contain a very large amount of vertices and for that, it is necessary to maintain efficient running time.
To do so we need data structures where all vertices can be accessed efficiently. 
Therefore, the appropriate data structure for performing operations on a very large list of nodes is HashMap. 
1. HashMap for nodes 
2. HashMap for edges where the key is String that contains the src and dest of the edge ...
- 

### Methods :
#### DWGraph :
- getNode-Return vertex by key ,complexity O(1)
- getEdge -Return edge between 2 vertices - performed by checking the existence of one vertex in the list of neighbors .
- addNode -Adding (to each HashMap) is in complexity O(1).
- connect - connects an edge with weight w between node src to dest .
- nodeIter , edgeIter- Iterators for nodes and edges in class.
- edgeIter(node_id)-Iterator for edges getting out of given node .
- removeNode , removeEdge  in complexity O(1).
- getters of nodesize ,edgeSize ,getMc.


#### DWG_Algo :
This class represents the algorithms of Graph Theory (directed weighted graph).
Some of the algorithms implemented using dijkstra algorithm.
```
. Dikstra Algorithm loop:
   * As long as there are any unvisited vertices:
   * Mark the X vertex as visited. (current vertex. In the first iteration this is the vertex of the source S)
   * For each vertex Y which is a neighbor of X and we have not yet visited it:
        Y is updated so that its distance is equal to the minimum value between two values: between its current distance,
        and the weight of the edge connecting X and Y plus the distance between S and X.
   * Select a new vertex X as the vertex whose distance from the source S is the shortest (at this point) from all the
     vertices in the graph we have not yet visited.
 The algorithm ends when the new vertex X is the destination or (to find all the fastest paths) when we have visited all the vertices.

Complexity of this algorithm is : O(v+e) where v=vertices, e=edges of the graph.
```
- The Main  functions  performed:
  - **init :** Initializes the class .
  - **copy:** Deep copy to graph - In this method the implementation made using copy constructor on directed_weighted_graph Class.
  - **Check if the graph is connected :** in this function we used BFS Algorithm
  - **shortestPath:** It returns the vertices  and the length of the shortest path,In this function we used the dijkstra algorithm.
  - **tsp :** Computes a list of consecutive nodes which go over all the nodes in cities.
  - **Save :** the graph as to an json file.
  - **Load :** the graph from an json file.







  

