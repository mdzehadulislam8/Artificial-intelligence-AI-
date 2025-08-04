class UndirectedGraph:
    def __init__(self):
        self.adjacency_list = {}

    def insert_edge(self, region_a, region_b):
        if region_a not in self.adjacency_list:
            self.adjacency_list[region_a] = []
        if region_b not in self.adjacency_list:
            self.adjacency_list[region_b] = []
        self.adjacency_list[region_a].append(region_b)
        self.adjacency_list[region_b].append(region_a)

    def is_valid_color(self, region, assigned_colors, current_color):
        for adjacent in self.adjacency_list[region]:
            if assigned_colors.get(adjacent, 0) == current_color:
                return False
        return True

    def backtrack_coloring(self, regions, idx, max_colors, assigned_colors):
        if idx == len(regions):
            return True
        region = regions[idx]
        for color in range(1, max_colors + 1):
            if self.is_valid_color(region, assigned_colors, color):
                assigned_colors[region] = color
                if self.backtrack_coloring(regions, idx + 1, max_colors, assigned_colors):
                    return True
                assigned_colors[region] = 0
        return False

    def solve_graph_coloring(self, max_colors):
        regions = list(self.adjacency_list.keys())
        assigned_colors = {}
        if self.backtrack_coloring(regions, 0, max_colors, assigned_colors):
            print("Valid Coloring Found:", assigned_colors)
        else:
            print("No Valid Coloring Possible")

if __name__ == "__main__":
    territory_map = UndirectedGraph()
    territory_map.insert_edge("WA", "NT")
    territory_map.insert_edge("WA", "SA")
    territory_map.insert_edge("NT", "SA")
    territory_map.insert_edge("NT", "QLD")
    territory_map.insert_edge("SA", "QLD")
    territory_map.insert_edge("SA", "NSW")
    territory_map.insert_edge("SA", "VIC")
    territory_map.insert_edge("QLD", "NSW")
    territory_map.insert_edge("NSW", "VIC")

    max_colors = 3
    territory_map.solve_graph_coloring(max_colors)