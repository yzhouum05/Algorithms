
# coding: utf-8

# # Depth-First Search
# Depth First Search
# 
# Example: Binary Tree Level-Order Traversal


def dfs_iterative(graph, start):
    # graph: dict, adjacent nodes to each node
    # start: node that traversal starts
    # return a list of all the nodes traversed
    
    visited, stack = [], [start] 
    while stack:
        vertex = stack.pop()
        if vertex not in visited: 
            visited.append(vertex)
            stack.extend(graph[start] - set(visited))
    return visited


def dfs_recursive(graph, start, visited = None):
    if not visited: visited = []
    visited.append(start)
    for vertex in graph[start] - set(visited):
        dfs_recursive(graph, vertex, visited)
    return visited


# Test Example:
# adjacency list
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

print(dfs_iterative(graph, 'A'))
print(dfs_recursive(graph, 'A'))

