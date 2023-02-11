'''
***************************************************************
Group Assignment 01
CS 534 - Team 6
Spring 2023

D. Veilleux

***************************************************************
'''


# Import Romania Map Data
import romania_map_data

map_data = romania_map_data.romania_map
map_locations = romania_map_data.romania_map.locations

import heapq

class SimpleProblemSolvingAgent:
    """
    SPSA class used to instantiate an object to find the best path
    between any two cities.
    To instantiate the class a Graph object is require argument
    """
    def __init__(self, graph, locations):
        self.graph = graph
        self.locations = locations
        # self.visited_city = []

    def heuristic_func(self, start, end):
        """
        Add a function to estimate the distance from the current city
        (queue) to the end city.
        :param start:
        :param end:
        :return:
        """
        x1, y1 = self.locations[start]
        x2, y2 = self.locations[end]
        return ((x1-x2)**2 + (y1-y2)**2) ** 0.5

    def search(self, start, end, strategy):
        """
        -Perform a search from the start city (initial state) to the
        destination city (end state).
        :param start: starting city
        :param end: destination city
        :param strategy: search algo.:
            BFS - best first search
            A* - astar search
        :return: route from start to end if it exists, else -> None
        """
        if start == end:
            return [start]
        # self.visited_city = []
        queue = [[start]]
        if strategy.upper() == 'BFS':
            return self.best_first_search(start, end)
        elif strategy.upper() == 'ASTAR':
            return self.astar(queue, end)
        else:
            return None

    def best_first_search(self, queue, end):
        # Create a priority queue for cities visited
        queue = [(0, queue, [queue])]
        # track the cities visited thru the search
        visited = set()

        while queue:
            # Pop the city (node) with the lowest cost
            (cost, node, path) = heapq.heappop(queue)
            # Check is the city has already been visited
            if node in visited:
                continue
            # Add the node to the visited set
            visited.add(node)
            # Check if the node is the destination city (end)
            # if so return the route (path)
            if node == end:
                return path
            # add the neighboring city of the current to the queue
            for neighbor in self.graph.get(node).keys():
                # Use the heuristic function to calculate distance (cost)
                cost = self.heuristic_func(neighbor, end)
                heapq.heappush(queue, (cost, neighbor, path + [neighbor]))
        return None

    def astar(self, queue, end):
        pass



### --- Testing Section --- ###

start_city = "Arad"
end_city = "Bucharest"
search_strategy = "bfs"

problem = SimpleProblemSolvingAgent(map_data, map_locations)
route = problem.search(start_city, end_city, search_strategy)

if route is not None:
    print("Route found: ", route)
else:
    print("Route not found.")









