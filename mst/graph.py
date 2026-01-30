import numpy as np
import heapq
from typing import Union

class Graph:

    def __init__(self, adjacency_mat: Union[np.ndarray, str]):
        """
    
        Unlike the BFS assignment, this Graph class takes an adjacency matrix as input. `adjacency_mat` 
        can either be a 2D numpy array of floats or a path to a CSV file containing a 2D numpy array of floats.

        In this project, we will assume `adjacency_mat` corresponds to the adjacency matrix of an undirected graph.
    
        """
        if type(adjacency_mat) == str:
            self.adj_mat = self._load_adjacency_matrix_from_csv(adjacency_mat)
        elif type(adjacency_mat) == np.ndarray:
            self.adj_mat = adjacency_mat
        else: 
            raise TypeError('Input must be a valid path or an adjacency matrix')
        self.mst = None

    def _load_adjacency_matrix_from_csv(self, path: str) -> np.ndarray:
        with open(path) as f:
            return np.loadtxt(f, delimiter=',')

    def construct_mst(self):
        """
    
        TODO: Given `self.adj_mat`, the adjacency matrix of a connected undirected graph, implement Prim's 
        algorithm to construct an adjacency matrix encoding the minimum spanning tree of `self.adj_mat`. 
            
        `self.adj_mat` is a 2D numpy array of floats. Note that because we assume our input graph is
        undirected, `self.adj_mat` is symmetric. Row i and column j represents the edge weight between
        vertex i and vertex j. An edge weight of zero indicates that no edge exists. 
        
        This function does not return anything. Instead, store the adjacency matrix representation
        of the minimum spanning tree of `self.adj_mat` in `self.mst`. We highly encourage the
        use of priority queues in your implementation. Refer to the heapq module, particularly the 
        `heapify`, `heappop`, and `heappush` functions.

        """
        # Number of vertices in the graph (adjacency matrix is n x n)
        n = self.adj_mat.shape[0]
        # Handle empty graph edge case
        if n == 0:
            self.mst = np.zeros_like(self.adj_mat)
            return

        # MST adjacency matrix to populate
        mst = np.zeros_like(self.adj_mat)
        # Track which vertices have been added to the MST
        visited = [False] * n
        # Start Prim's algorithm from vertex 0
        visited[0] = True

        # Min-heap of candidate edges (weight, from_vertex, to_vertex)
        heap = []
        # Seed the heap with edges from the starting vertex
        for v in range(n):
            w = self.adj_mat[0, v]
            if w > 0:
                heapq.heappush(heap, (w, 0, v))

        # Count how many edges have been added to the MST
        edges_used = 0
        # Continue until MST has n-1 edges or no candidates remain
        while heap and edges_used < n - 1:
            # Always pick the lightest available edge
            w, u, v = heapq.heappop(heap)
            # Skip if the destination is already in the MST
            if visited[v]:
                continue
            # Add the new vertex and its connecting edge to the MST
            visited[v] = True
            mst[u, v] = w
            mst[v, u] = w
            edges_used += 1

            # Push all outgoing edges from the newly added vertex
            for nxt in range(n):
                w_next = self.adj_mat[v, nxt]
                if not visited[nxt] and w_next > 0:
                    heapq.heappush(heap, (w_next, v, nxt))

        # Store the constructed MST adjacency matrix
        self.mst = mst
