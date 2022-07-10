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
        nodes = self.getNodes(node)              # ----- get all nodes in a set
        
        mapping = {}                             # ----- use hash map to store old:new value pair
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

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:


        # Create graph [1,0], [2,1]
        # edges: [1] > [2] > []
        # in degree: [0, 1, 1] 
        edges = [[] for i in range(numCourses)] # index = course, value in the list = next course
        degrees = [0] * numCourses # store the number of in degree
        for course, pre_course in prerequisites:
            edges[pre_course].append(course) # add next course 
            degrees[course] += 1# add in degree

        # BFS
        # 1,0 | 2,1 | 3,1
        # queue(1)
        queue = collections.deque(course for course, degree in enumerate(degrees) if not degree) # add course which in degree == 0
        while queue:
            course = queue.popleft() # course = 1
            for next_course in edges[course]: #loop through all next courses
                degrees[next_course] -= 1 # decrease in degree
                if not degrees[next_course]: # if next course's in degree == 0
                    queue.append(next_course) # add to the queue

        return not sum(degrees)

    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 0:        # no integer
            return False
        if len(edges) != n-1: # if number of edges doesn't equal to number of nodes - 1
            return False

        g = {}
        for e in edges:
            g[e[0]] = g.get(e[0], []) + [e[1]]    # add all neighbors
            g[e[1]] = g.get(e[1], []) + [e[0]]
        q = [0]        # always start with 0
        visited = set([0])

        # make sure all nodes in edges got visited
        while q:
            node = q.pop(0)
            for i in g.get(node, []):
                if i in visited:
                    continue
                q.append(i)
                visited.add(i)
        return len(visited) == n

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
            # corner case
            if not heights:
                return []
            
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            nodes_visited_times = {}
            res = []
            paci_position, alta_position = self.get_start_position(heights)
            
            self.bfs(heights, directions, nodes_visited_times, paci_position)
            self.bfs(heights, directions, nodes_visited_times, alta_position)
            
            for key, val in nodes_visited_times.items():
                if val == 2:
                    res.append(list(key))
            return res
        
    def get_start_position(self, heights):
        m, n = len(heights), len(heights[0])
        paci_position = []
        alta_position = []
        for i in range(m):
            for j in range(n):
                if j == 0 or i == 0:
                    paci_position.append((i,j))
                if i == m-1 or j == n-1:
                    alta_position.append((i,j))
        return paci_position, alta_position    
            
    def bfs(self, heights, directions, nodes_visited_times, start_position):  
        queue = deque(start_position)
        visited = set(start_position)
        
        while queue:
            cur_posi = queue.popleft()
            nodes_visited_times[cur_posi] = nodes_visited_times.get(cur_posi, 0) + 1
            for deltaX, deltaY in directions:
                newX = cur_posi[0] + deltaX
                newY = cur_posi[1] + deltaY
                if not self.is_valid(heights, visited, cur_posi[0], cur_posi[1], newX, newY):
                    continue
                visited.add((newX, newY))
                queue.append((newX, newY))
                
                   
    def is_valid(self, heights, visited, i, j, newX, newY):    
        return 0 <= newX < len(heights) and 0<= newY < len(heights[0]) and (newX, newY) not in visited and heights[newX][newY] >= heights[i][j]
        # valid means 1. new cell within the bound 2. I haven't visited the new cell 3. the new cell value is greater or equal to current cell
