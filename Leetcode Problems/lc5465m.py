"""
5465. Number of Nodes in the Sub-Tree With the Same Label

Given a tree (i.e. a connected, undirected graph that has no cycles) consisting of n nodes numbered from 0 to n - 1 and
exactly n - 1 edges. The root of the tree is the node 0, and each node of the tree has a label which is a lower-case
character given in the string labels (i.e. The node with the number i has the label labels[i]).

The edges array is given on the form edges[i] = [ai, bi], which means there is an edge between nodes ai and bi in the
tree.

Return an array of size n where ans[i] is the number of nodes in the subtree of the ith node which have the same label
as node i.

A subtree of a tree T is the tree consisting of a node in T and all of its descendant nodes.
"""


def countSubTrees(n, edges, labels):
    """
    TLE
    """
    def dfs(v, o, l):
        if labels[v] == l:
            count[o] += 1
        for x in aj[v]:
            dfs(x, o, l)

    aj = [[] for _ in range(n)]
    count = [0 for _ in range(n)]
    added = {0}
    for e in edges:
        if e[1] not in added:
            aj[e[0]].append(e[1])
            added.add(e[1])
        else:
            aj[e[1]].append(e[0])
            added.add(e[0])
    for v in range(n):
        dfs(v, v, labels[v])

    return count


# n = 7
# ed = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]]
# la = "abaedcd"
# print(countSubTrees(n,ed,la) == [2,1,1,1,1,1,1])

# n = 4
# ed = [[0,2],[0,3],[1,2]]
# la = "aeed"
# print(countSubTrees(n,ed,la) == [1,1,2,1])

n = 25
ed = [[4, 0], [5, 4], [12, 5], [3, 12], [18, 3], [10, 18], [8, 5], [16, 8], [14, 16], [13, 16], [9, 13], [22, 9],
      [2, 5], [6, 2], [1, 6], [11, 1], [15, 11], [20, 11], [7, 20], [19, 1], [17, 19], [23, 19], [24, 2], [21, 24]]
la = "hcheiavadwjctaortvpsflssg"
print(countSubTrees(n, ed, la) == [2, 2, 1, 1, 1, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1])
