__author__ = 'zhewang711'


class Node:

    def __init__(self, elem):
        self.elem = elem
        self.towards = None


class Graph:

    def __init__(self, table):
        self.vertices = {}
        self.outgoing = {}
        self.grid = None
        self.table = table

    def transform(self, grid):
        self.grid = grid
        for i in range(len(grid) - 1):
            for j in range(len(grid[0]) - 1):
                id = i * len(grid[0]) + j
                if self.outgoing.get(id) is None:
                    self.outgoing[id] = {}
                    self.vertices[id] = (i, j)
                self.outgoing[id][id + 1] = grid[i][j + 1]
                self.outgoing[id][id + len(grid[0])] = grid[i + 1][j]

        i = len(grid) - 1
        for j in range(len(grid[0]) - 1):
            id = i * len(grid[0]) + j
            if self.outgoing.get(id) is None:
                self.outgoing[id] = {}
                self.vertices[id] = (i, j)
            self.outgoing[id][id + 1] = grid[i][j + 1]

        j = len(grid[0]) - 1
        for i in range(len(grid) - 1):
            id = i * len(grid[0]) + j
            if self.outgoing.get(id) is None:
                self.outgoing[id] = {}
                self.vertices[id] = (i, j)
            self.outgoing[id][id + len(grid[0])] = grid[i + 1][j]

        self.outgoing[len(grid)*len(grid[0]) - 1] = {}
        self.vertices[len(grid)*len(grid[0]) - 1] = (len(grid) - 1, len(grid[0]) - 1)

    def find_min(self, current_edges, distance):
        choice = 0
        for i in range(len(current_edges)):
            if current_edges[i][2] + distance[current_edges[i][0]] < current_edges[choice][2] + distance[current_edges[choice][0]]:
                choice = i
        tmp = current_edges[choice]
        i = len(current_edges) - 1
        while i >= 0:
            if current_edges[i][1] == tmp[1]:
                del current_edges[i]
            i -= 1
        return tmp

    def dijkstra(self):
        distance = [None] * len(self.vertices)
        distance[0] = self.grid[0][0]
        current_vertex = {1: self.grid[0][0] + self.outgoing[0][1], len(self.grid[0]): self.grid[0][0]+self.outgoing[0][len(self.grid[0])]}
        cnt = 0
        while distance[-1] is None:
            choice = None
            dis = float('inf')
            for vertex, dist in current_vertex.items():
                if dist < dis:
                    dis = dist
                    choice = vertex
            distance[choice] = dis
            del current_vertex[choice]

            for vertex, weight in self.outgoing[choice].items():
                if current_vertex.get(vertex) is None:
                    current_vertex[vertex] = dis + weight
                else:
                    current_vertex[vertex] = min(current_vertex[vertex], dis + weight)
        return distance[-1]


class Solution(object):


    def DP(self, grid):
        if len(grid) == 1:
            return sum(grid[0])
        elif len(grid[0]) == 1:
            the_sum = 0
            for i in range(len(grid)):
                the_sum += grid[i][0]
            return the_sum
        else:
            table = [[None for i in range(len(grid[0]))] for i in range(len(grid))]
            table[0][0] = grid[0][0]
            i = 0
            for j in range(1, len(grid[0])):
                table[i][j] = grid[i][j] + table[i][j - 1]
            j = 0
            for i in range(1, len(grid)):
                table[i][j] = grid[i][j] + table[i - 1][j]
            for i in range(1, len(grid)):
                for j in range(1, len(grid[0])):
                    table[i][j] = grid[i][j] + min(table[i][j-1], table[i-1][j])
            return table


    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        return self.DP(grid)

    def minPathSum2(self, table, grid):
        g = Graph(table)
        g.transform(grid)
        return g.dijkstra()


if __name__ == '__main__':
    table = Solution().minPathSum([[8,1,6,3,6,2,2,7,1,9,9,0,3,3,5,0,3,1,1],[1,3,5,8,7,9,9,6,0,2,9,1,0,2,8,6,8,2,8],[6,3,0,5,6,5,0,3,5,3,4,6,6,7,3,6,7,5,5],[3,7,0,4,9,2,6,9,0,4,1,9,2,7,1,9,5,6,9],[8,1,2,4,8,8,3,3,5,0,8,2,5,6,4,9,5,7,5],[6,7,2,9,8,6,6,9,6,1,5,5,1,7,0,7,7,0,3],[0,5,5,1,0,1,7,4,0,4,3,8,0,3,2,9,1,8,8],[3,4,1,8,2,5,7,2,2,6,2,7,9,0,3,0,2,4,7],[8,6,1,2,6,3,7,8,2,8,7,2,1,3,4,2,5,9,9],[9,3,8,4,1,7,4,6,7,8,2,6,6,0,9,0,7,2,7],[7,6,8,4,9,1,0,3,3,5,4,5,7,7,3,1,0,0,7],[8,9,5,0,5,3,1,4,6,0,8,3,7,4,3,4,3,5,4],[8,8,1,2,3,0,0,8,1,2,0,0,1,9,5,3,6,1,6]])
    print(table[-1][-1])
    print(Solution().minPathSum2(table,[[8,1,6,3,6,2,2,7,1,9,9,0,3,3,5,0,3,1,1],[1,3,5,8,7,9,9,6,0,2,9,1,0,2,8,6,8,2,8],[6,3,0,5,6,5,0,3,5,3,4,6,6,7,3,6,7,5,5],[3,7,0,4,9,2,6,9,0,4,1,9,2,7,1,9,5,6,9],[8,1,2,4,8,8,3,3,5,0,8,2,5,6,4,9,5,7,5],[6,7,2,9,8,6,6,9,6,1,5,5,1,7,0,7,7,0,3],[0,5,5,1,0,1,7,4,0,4,3,8,0,3,2,9,1,8,8],[3,4,1,8,2,5,7,2,2,6,2,7,9,0,3,0,2,4,7],[8,6,1,2,6,3,7,8,2,8,7,2,1,3,4,2,5,9,9],[9,3,8,4,1,7,4,6,7,8,2,6,6,0,9,0,7,2,7],[7,6,8,4,9,1,0,3,3,5,4,5,7,7,3,1,0,0,7],[8,9,5,0,5,3,1,4,6,0,8,3,7,4,3,4,3,5,4],[8,8,1,2,3,0,0,8,1,2,0,0,1,9,5,3,6,1,6]]))
