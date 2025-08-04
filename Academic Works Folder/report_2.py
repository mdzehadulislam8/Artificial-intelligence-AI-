class DirectedGraph:
    def __init__(self):
        self.adjacency_list = {}

    def insert_edge(self, start, end):
        if start not in self.adjacency_list:
            self.adjacency_list[start] = []
        self.adjacency_list[start].append(end)

    def dfs_helper(self, vertex, visited_nodes, sorted_stack):
        visited_nodes.add(vertex)
        if vertex in self.adjacency_list:
            for adjacent in self.adjacency_list[vertex]:
                if adjacent not in visited_nodes:
                    self.dfs_helper(adjacent, visited_nodes, sorted_stack)
        sorted_stack.append(vertex)

    def perform_topological_sort(self):
        visited_nodes = set()
        sorted_stack = []
        for vertex in self.adjacency_list:
            if vertex not in visited_nodes:
                self.dfs_helper(vertex, visited_nodes, sorted_stack)
        return sorted_stack[::-1]

if __name__ == "__main__":
    graph = DirectedGraph()
    graph.insert_edge(7, 3)
    graph.insert_edge(7, 1)
    graph.insert_edge(5, 0)
    graph.insert_edge(5, 2)
    graph.insert_edge(3, 4)
    graph.insert_edge(4, 4)

    sorted_result = graph.perform_topological_sort()
    print("Topological Sort:", sorted_result)
