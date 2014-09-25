"""Kruskal.py
Author: BO WANG
Date: 09/18/2014

Kruskal's algorithm for MST using Union-find structure to reduce complexity"""

from UnionFind import UnionFind


def kruskal(G):
    """ Return MST of the given undirected graph"""
    sumWeight = 0
    # Sort edges by weights. If root(u) != root(v), add the edge to MST
    uf = UnionFind()
    # tree = []
    for W, u, v in sorted((G[u][v], u, v) for u in G for v in G[u]):
        if uf[u] != uf[v]:
            # tree.append((u,v))
            uf.union(u,v)
            sumWeight += G[u][v]
    return sumWeight
