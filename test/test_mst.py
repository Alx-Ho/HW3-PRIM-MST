import pytest
import numpy as np
from mst import Graph
from sklearn.metrics import pairwise_distances


def check_mst(adj_mat: np.ndarray, 
              mst: np.ndarray, 
              expected_weight: int, 
              allowed_error: float = 0.0001):
    """
    
    Helper function to check the correctness of the adjacency matrix encoding an MST.
    Note that because the MST of a graph is not guaranteed to be unique, we cannot 
    simply check for equality against a known MST of a graph. 

    Arguments:
        adj_mat: adjacency matrix of full graph
        mst: adjacency matrix of proposed minimum spanning tree
        expected_weight: weight of the minimum spanning tree of the full graph
        allowed_error: allowed difference between proposed MST weight and `expected_weight`

    TODO: Add additional assertions to ensure the correctness of your MST implementation. For
    example, how many edges should a minimum spanning tree have? Are minimum spanning trees
    always connected? What else can you think of?

    """

    def approx_equal(a, b):
        return abs(a - b) < allowed_error

    # Same dimensions as the original graph.
    assert adj_mat.shape == mst.shape, 'MST must have same shape as adjacency matrix'
    # Undirected MST should be symmetric.
    assert np.allclose(mst, mst.T), 'MST adjacency matrix must be symmetric'
    # MST edges must be a subset of the original graph's edges.
    assert np.all((mst == 0) | np.isclose(mst, adj_mat, atol=allowed_error)), (
        'MST must only use edges from original graph'
    )

    total = 0
    edge_count = 0
    for i in range(mst.shape[0]):
        for j in range(i+1):
            total += mst[i, j]
            if mst[i, j] > 0:
                edge_count += 1
    # A spanning tree on n nodes has exactly n-1 edges.
    assert edge_count == mst.shape[0] - 1, 'MST must have exactly n-1 edges'

    # Connectivity check via BFS on mst
    n = mst.shape[0]
    visited = [False] * n
    stack = [0]
    visited[0] = True
    while stack:
        u = stack.pop()
        for v in range(n):
            if mst[u, v] > 0 and not visited[v]:
                visited[v] = True
                stack.append(v)
    # A valid MST must connect all vertices.
    assert all(visited), 'MST must be connected'
    # Total MST weight should match expected weight.
    assert approx_equal(total, expected_weight), 'Proposed MST has incorrect expected weight'


def test_mst_small():
    """
    
    Unit test for the construction of a minimum spanning tree on a small graph.
    
    """
    file_path = './data/small.csv'
    g = Graph(file_path)
    g.construct_mst()
    check_mst(g.adj_mat, g.mst, 8)


def test_mst_single_cell_data():
    """
    
    Unit test for the construction of a minimum spanning tree using single cell
    data, taken from the Slingshot R package.

    https://bioconductor.org/packages/release/bioc/html/slingshot.html

    """
    file_path = './data/slingshot_example.txt'
    coords = np.loadtxt(file_path) # load coordinates of single cells in low-dimensional subspace
    dist_mat = pairwise_distances(coords) # compute pairwise distances to form graph
    g = Graph(dist_mat)
    g.construct_mst()
    check_mst(g.adj_mat, g.mst, 57.263561605571695)


def test_mst_student():
    """
    
    TODO: Write at least one unit test for MST construction.
    
    """
    # 4-node cycle with equal-weight edges (1) and heavier diagonals (2).
    # Multiple MSTs exist here; any three cycle edges give the same total weight.
    # This checks that the implementation handles ties and still returns a valid MST.
    adj = np.array(
        [
            [0, 1, 2, 1],
            [1, 0, 1, 2],
            [2, 1, 0, 1],
            [1, 2, 1, 0],
        ],
        dtype=float,
    )
    g = Graph(adj)
    g.construct_mst()
    check_mst(g.adj_mat, g.mst, 3)
