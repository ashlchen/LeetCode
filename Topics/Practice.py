
"""
1,0 Grid
1 > land 
count number of island
all edges are water

[[1]] > 1
[[]] > 0 
[[0]] > 0

constraints?
0 <= m,n < 1000
m = width
n = length
"""

#DFS
"""
result=0

main function
traverse through the graph
    if current node = 1
        increment counter
        call DFS on current node

return result

def dfs(current node)
    if current node = 0
        return
    change current node into 0
    call dfs to neighbor

"""


def main(graph):
    l = len(graph)
    w = len(graph[0])
    result = 0

    for i in range(l):
        for j in range(w):
            if graph[i][j] == 1:
                result += 1
                dfs(graph, i, j)

    return result

def dfs(graph, i, j):
    if i < 0 or i >= len(graph) or j < 0 or j >= len(graph[0]) or graph[i][j] == 0:
        return

    graph[i][j] = 0
    dfs(graph, i-1,j)
    dfs(graph, i,j-1)
    dfs(graph, i+1,j)
    dfs(graph, i,j+1)

print(main([[1]]))
print(main([[0]]))
print(main([[1,0,1],[1,0,1]]))
print(main([[0,0,1]]))
print(main([[1,1,1],[1,0,0],[0,0,1]]))
print(main([[]]))

