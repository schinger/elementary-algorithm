def SED(X, Y):
    """Compute the squared Euclidean distance between X and Y."""
    return sum((i-j)**2 for i, j in zip(X, Y))
import collections
import operator

def nearest_neighbor_bf(*, query_points, reference_points):
    """Use a brute force algorithm to solve the
    "Nearest Neighbor Problem".
    """
    return {
        query_p: min(
            reference_points,
            key=lambda X: SED(X, query_p),
        )
        for query_p in query_points
    }

BT = collections.namedtuple("BT", ["value", "left", "right"])
BT.__doc__ = """
A Binary Tree (BT) with a node value, and left- and
right-subtrees.
"""

def kdtree(points):
    """Construct a k-d tree from an iterable of points.
    
    This algorithm is taken from Wikipedia. For more details,
    
    > https://en.wikipedia.org/wiki/K-d_tree#Construction
    
    """
    k = len(points[0])
    
    def build(*, points, depth):
        """Build a k-d tree from a set of points at a given
        depth.
        """
        if len(points) == 0:
            return None
        
        points.sort(key=operator.itemgetter(depth % k))
        middle = len(points) // 2
        
        return BT(
            value = points[middle],
            left = build(
                points=points[:middle],
                depth=depth+1,
            ),
            right = build(
                points=points[middle+1:],
                depth=depth+1,
            ),
        )
    
    return build(points=list(points), depth=0)

NNRecord = collections.namedtuple("NNRecord", ["point", "distance"])
NNRecord.__doc__ = """
Used to keep track of the current best guess during a nearest
neighbor search.
"""

def find_nearest_neighbor(*, tree, point):
    """Find the nearest neighbor in a k-d tree for a given
    point.
    """
    k = len(point)
    
    best = None
    def search(*, tree, depth):
        """Recursively search through the k-d tree to find the
        nearest neighbor.
        """
        nonlocal best
        
        if tree is None:
            return
        
        distance = SED(tree.value, point)
        if best is None or distance < best.distance:
            best = NNRecord(point=tree.value, distance=distance)
        
        axis = depth % k
        diff = point[axis] - tree.value[axis]
        if diff <= 0:
            close, away = tree.left, tree.right
        else:
            close, away = tree.right, tree.left
        
        search(tree=close, depth=depth+1)
        if diff**2 < best.distance:
            search(tree=away, depth=depth+1)
    
    search(tree=tree, depth=0)
    return best.point
def nearest_neighbor_kdtree(*, query_points, reference_points):
    """Use a k-d tree to solve the "Nearest Neighbor Problem"."""
    tree = kdtree(reference_points)
    return {
        query_p: find_nearest_neighbor(tree=tree, point=query_p)
        for query_p in query_points
    }
    
    
    
import random

random_point = lambda: (random.random(), random.random())
reference_points = [ random_point() for _ in range(10) ]
query_points = [ random_point() for _ in range(10) ]

solution_bf = nearest_neighbor_bf(
    reference_points = reference_points,
    query_points = query_points
)
solution_kdtree = nearest_neighbor_kdtree(
    reference_points = reference_points,
    query_points = query_points
)

solution_bf == solution_kdtree


######k(m)-NN
def nearest_neighbor_bf_m(*, query_points, reference_points, m):
    """Use a brute force algorithm to solve the
    "Nearest Neighbor Problem".
    """
    return {
        query_p: sorted(reference_points, key=lambda X: SED(X, query_p))[:m]
        for query_p in query_points
    }


def find_nearest_neighbor_m(*, tree, point, m):
    """Find the nearest neighbor in a k-d tree for a given
    point.
    """
    k = len(point)
    nn = [NNRecord(point=None, distance=float('inf'))]*m
    def search(*, tree, depth):
        """Recursively search through the k-d tree to find the
        nearest neighbor.
        """
        nonlocal nn
        
        if tree is None:
            return
        
        distance = SED(tree.value, point)
        if distance < nn[-1].distance:
            nn.append(NNRecord(point=tree.value, distance=distance))
            nn.sort(key=operator.itemgetter(1))
            nn.pop()

        axis = depth % k
        diff = point[axis] - tree.value[axis]
        if diff <= 0:
            close, away = tree.left, tree.right
        else:
            close, away = tree.right, tree.left
        
        search(tree=close, depth=depth+1)
        if diff**2 < nn[-1].distance:
            search(tree=away, depth=depth+1)
    
    search(tree=tree, depth=0)
    return [e.point for e in nn]

def nearest_neighbor_kdtree_m(*, query_points, reference_points, m):
    """Use a k-d tree to solve the "Nearest Neighbor Problem"."""
    tree = kdtree(reference_points)
    return {
        query_p: find_nearest_neighbor_m(tree=tree, point=query_p, m=m)
        for query_p in query_points
    }
    

random_point = lambda: (random.random(), random.random(), random.random())
reference_points = [ random_point() for _ in range(100) ]
query_points = [ random_point() for _ in range(100) ]

solution_bf = nearest_neighbor_bf_m(
    reference_points = reference_points,
    query_points = query_points,
    m = 12
)
solution_kdtree = nearest_neighbor_kdtree_m(
    reference_points = reference_points,
    query_points = query_points,
    m = 12
)

solution_bf == solution_kdtree
