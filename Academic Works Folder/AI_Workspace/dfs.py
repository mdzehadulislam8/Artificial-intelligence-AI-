def robot_topological_sort(matrix):

    def dfs_sort(graph):
        def explore(node):
            if node in visited_nodes:
                return
            visited_nodes.add(node)
            for neighbor in graph[node]:
                explore(neighbor)

            sorted_order.insert(0, node)

        visited_nodes = set()
        sorted_order = []

        for node in graph.keys():
            if node not in visited_nodes:
                explore(node)

        return sorted_order

    total_rows, total_cols = len(matrix), len(matrix[0])
    adjacency_list = {}

    for row in range(total_rows):
        for col in range(total_cols):
            if matrix[row][col] == 1:
                current_cell = (row, col)
                adjacent_cells = []

                if row - 1 >= 0 and matrix[row - 1][col] == 1:

                    adjacent_cells.append((row - 1, col))

                if row + 1 < total_rows and matrix[row + 1][col] == 1:


                    adjacent_cells.append((row + 1, col))

                if col - 1 >= 0 and matrix[row][col - 1] == 1:

                    adjacent_cells.append((row, col - 1))

                if col + 1 < total_cols and matrix[row][col + 1] == 1:
                    
                    adjacent_cells.append((row, col + 1))

                adjacency_list[current_cell] = adjacent_cells

    return dfs_sort(adjacency_list)


matrix = [
    [1, 1, 0, 1],
    [1, 0, 1, 0],
    [1, 0, 0, 1],
    [0, 1, 0, 1],
    [1, 1, 1, 0],
    [1, 1, 0, 1]
    
]


topological_order = robot_topological_sort(matrix)
print("Topological Order:", topological_order)
