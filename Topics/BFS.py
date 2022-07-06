class Solution:
    def topSort(self, graph):
        node_to_indegree = self.get_indegree(graph)

        #bfs
        order = []
        start_nodes = [n for n in graph if node_to_indegree[n] == 0]
        queue = collections.deque(start_nodes)
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in node.neighbors:
                node_to_indegree[neighbor] -= 1
                if node_to_indegree[neighbor] == 0:
                    queue.append(neighbor)

        if len(order) != len(graph):
            return []
        return order

    def get_indegree(self, graph):
        node_to_indegree = {x: 0 for x in graph}

        for node in graph:
            for neighbor in node.neighbors:
                node_to_indegree[neighbor] += 1

        return node_to_indegree

    def numIslands(self, grid: List[List[str]]) -> int:
            island = 0
            visited = set()
            #loop through the graph
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] != "1" or (i,j) in visited:
                        continue
                    island += 1
                    visited.add((i,j))
                    self.bfs(grid,i,j,visited)
            return island
        
    #bfs to find connected places
    def bfs(self, grid, x, y, visited):
        queue = collections.deque([(x,y)])
        
        while queue:
            x, y = queue.popleft()
            for deltaX, deltaY in [(1,0),(0,1),(-1,0),(0,-1)]:
                newX = x + deltaX
                newY = y + deltaY
                if not 0<=newX<len(grid) or not 0<=newY<len(grid[0]):
                    continue
                if (newX, newY) not in visited and grid[newX][newY] == "1":
                    visited.add((newX, newY))
                    queue.append([newX, newY])
        return

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        nodes = self.getNodes(node)
        
        mapping = {}
        for n in nodes:
            mapping[n] = Node(n.val)
            
        for n in nodes:
            newNode = mapping[n]
            for neighbor in n.neighbors:
                newNeighbor = mapping[neighbor]
                newNode.neighbors.append(newNeighbor)
                
        return mapping[node]
    
    # bfs - find all nodes   
    def getNodes(self, node):
        queue = deque([node])
        visited = set([node])
        while queue:
            head = queue.popleft()
            for neighbor in head.neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return visited