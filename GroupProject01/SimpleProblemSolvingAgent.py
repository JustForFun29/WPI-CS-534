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
from queue import PriorityQueue

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
            return self.astar_search(start, end)
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

    def astar_search(self, start, end):
        """
        A* search is best-first graph search used in pathfinding
        function used in A* is f(n) = g(n) + h(n)
        where g(n) is distance from starting node, h(n) is distance from end node
        :param start: starting city:
        :param end: destination city:
        :return: returns a Route from starting city to destination city
        """
        # Create priority queue for cities in the frontier (analogy of open set)
        frontier = PriorityQueue()
        # Add starting city as the first visited city
        frontier.put(start, 0)
        # Create two dictionaries to keep track of each cost/route
        came_from: dict[Location, Optional[Location]] = {}
        cost_so_far: dict[Location, float] = {}
        # Create set for visited cities
        visited = set();
        # Append information for starting city
        came_from[start] = None
        cost_so_far[start] = 0


        # Iterate through each city in the frontier
        while frontier:
            # Get the current city from the frontier
            current: Location = frontier.get()

            # If current city has already been visited
            if current in visited:
                continue

            # If goal state is reached - return the route
            if current == end:
                break

            # Iterate through all nodes available from current node
            for next in self.graph.get(current).keys():
                # F cost =        G cost              +  H cost
                cost = self.heuristic_func(next, start) + self.heuristic_func(next, end)
                new_cost = cost_so_far[current] + cost

                # If calculated cost has only been calculated or if calculated cost is smaller than previous one
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    # Assign calculated cost to the neighbor node
                    cost_so_far[next] = new_cost
                    # Add priority for the next neighbor
                    priority = new_cost + self.heuristic_func(next, end)
                    # Add next node to the priority queue with F cost
                    frontier.put(next, priority)
                    # Add current node to the list of visited cities
                    came_from[next] = current

        return came_from, cost_so_far

    def reconstruct_path(self, came_from, start, end):
        """
        Helper function
        :param came_from:
        :param start:
        :param end:
        :return:
        """
        reverse_path = [end]
        while end != start:
            end = came_from[end]
            reverse_path.append(end)
        return list(reversed(reverse_path))



### --- Testing Section --- ###

start_city = "Arad"
end_city = "Bucharest"
search_strategy = "astar"

problem = SimpleProblemSolvingAgent(map_data, map_locations)
route = problem.search(start_city, end_city, search_strategy)

# TODO: Only for testing purposes, will delete it later
if search_strategy == "astar":
    (came_from, cost_so_far) = route
    route = problem.reconstruct_path(came_from, start_city, end_city)



if route is not None:
    print("Route found: ", route)
else:
    print("Route not found.")









