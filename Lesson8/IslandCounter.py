class Archipelago:
    def __init__(self, row, col, graph):
        self.ROW = row
        self.COL = col
        self.graph = graph

    def searchable(self, i, j, visited):
        """
        Check if a given cell (row, col) can be included in DFS
        Return whether the row & column number is in range and the cell is not yet visited and value is not 0
        """
        return i >= 0 and i < self.ROW and j >= 0 and j < self.COL and not visited[i][j] and self.graph[i][j]

    def DFS(self, i, j, visited):
        """
        DFS the 8 neighbours (adjacent nodes) of a cell.
        """
        # Used to get row and column numbers of adjacent nodes
        row_idx = [-1, -1, -1,  0, 0,  1, 1, 1];
        col_idx = [-1,  0,  1, -1, 1, -1, 0, 1];
         
        # Mark this cell as visited
        visited[i][j] = True

        # Recur for all connected nodes
        for k in range(8):
            if self.searchable(i + row_idx[k], j + col_idx[k], visited):
                self.DFS(i + row_idx[k], j + col_idx[k], visited)

    def count_islands(self):
        # Bool matrix to mark visited cells.
        visited = [[False for j in range(self.COL)] for i in range(self.ROW)]

        islands = 0
        for i in range(self.ROW):
            for j in range(self.COL):
                # If a cell with value 1 is not yet visited, it's a new island
                if visited[i][j] == False and self.graph[i][j] == 1:
                    # Search for connected nodes and increament island count
                    self.DFS(i, j, visited)
                    islands += 1

        return islands


graph = [
    [ 1, 0, 0, 0, 1 ],
    [ 0, 1, 0, 0, 1 ],
    [ 0, 0, 1, 0, 0 ],
    [ 0, 0, 0, 1, 0 ],
    [ 1, 0, 1, 0, 0 ],
]

row = len(graph)
col = len(graph[0])

area = Archipelago(row, col, graph)
islands = area.count_islands()

print(str(islands) + " islands")
