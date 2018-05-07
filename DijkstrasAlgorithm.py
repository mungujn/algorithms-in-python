class Dijkstras:
    graph = {}
    costs = {}
    parents = {}
    processed = []

    def __init__(self):
        self.buildGraph()
        self.buildCosts()
        self.buildParents()

    def printShortestPath(self, start, node):
        solution = ""
        parent = ""
        while parent is not start:
            parent = self.parents[node]
            solution += parent
            node = parent
        return solution

    def findShortestPath(self):
        node = self.findLowestCostNode()
        while node is not None:
            cost = self.costs[node]
            neighbours = self.graph[node]
            for n in neighbours.keys():
                new_cost = cost + neighbours[n]
                if self.costs[n] > new_cost:
                    self.costs[n] = new_cost
                    self.parents[n] = node
            self.processed.append(node)
            node = self.findLowestCostNode()

    def findLowestCostNode(self):
        lowest_cost = float("inf")
        lowest_cost_node = None
        for node in self.costs:
            cost = self.costs[node]
            if cost < lowest_cost and node not in self.processed:
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node

    def buildGraph(self):
        self.graph["start"] = {}
        self.graph["start"]["a"] = 6
        self.graph["start"]["b"] = 2

        self.graph["a"] = {}
        self.graph["a"]["fin"] = 1

        self.graph["b"] = {}
        self.graph["b"]["a"] = 3
        self.graph["b"]["fin"] = 5

        self.graph["fin"] = 5

    def buildCosts(self):
        infinity = float("inf")

        self.costs["a"] = 6
        self.costs["b"] = 2
        self.costs["fin"] = infinity

    def buildParents(self):
        self.parents["a"] = "start"
        self.parents["b"] = "start"
        self.parents["fin"] = None