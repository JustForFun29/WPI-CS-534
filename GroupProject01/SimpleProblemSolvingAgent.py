from queue import PriorityQueue

class SimpleProblemSolvingAgent:
    def __init__(self, graph_file_name,locations_file_name, initial_location, goal_location):
        self.graph = self.import_graph(graph_file_name)
        self.locations = self.import_locations(locations_file_name)
        self.initial_location = initial_location
        self.goal_location = goal_location
        self.h = self.calculate_h()


    def city_validator(self):
        """Helper function for validating provided initial and goal locations, if they are in the graph
        function will return boolean value (True) otherwise (False)"""
        if (self.initial_location in self.graph) and (self.goal_location in self.graph) and (self.initial_location in self.locations) and (self.goal_location in self.locations):
            return True
        else:
            return False


    def import_locations(self, file_name):
        """Helper function for importing cities coordinates from given txt file.
        The format of the txt file should be: 'City1 x_coordinate y_coordinate'"""
        locations = {}
        file = open(file_name)
        for i in file.readlines():
            node = i.split()

            locations.update({node[0]: (int(node[1]), int(node[2]))})

        # print(locations)
        return locations

    def import_graph(self, graph_file_name):
        """Helper function for importing graph from given txt file.
        The format of the txt file should be: 'City1 City2 Distance'
        And it should include all the distances from each city to neighbouring city, if that path exists"""
        graph = {}
        file = open(graph_file_name)
        for i in file.readlines():
            node = i.split()

            if node[0] in graph and node[1] in graph:
                c = graph.get(node[0])
                c.append([node[1], node[2]])
                graph.update({node[0]: c})

                c = graph.get(node[1])
                c.append([node[0], node[2]])
                graph.update({node[1]: c})

            elif node[0] in graph:
                c = graph.get(node[0])
                c.append([node[1], node[2]])
                graph.update({node[0]: c})

                graph[node[1]] = [[node[0], node[2]]]

            elif node[1] in graph:
                c = graph.get(node[1])
                c.append([node[0], node[2]])
                graph.update({node[1]: c})

                graph[node[0]] = [[node[1], node[2]]]

            else:
                graph[node[0]] = [[node[1], node[2]]]
                graph[node[1]] = [[node[0], node[2]]]

        return graph


    def calculate_h(self):
        """"Function for calculating h(n) for each node within the graph
        and storing it in the dictionary"""
        heuristics = {}
        x2, y2 = self.locations[self.goal_location]
        for name, location in self.locations.items():
            x1, y1 = location
            current_h = int(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5)
            heuristics[name] = float(current_h)
        # print(heuristics)
        return heuristics


    def best_first_graph_search(self):
        """
        Performs search using - Best First Graph Search algorithm, that
        uses nodes with the lowest h(n) values and finds the route, if there is one
        :return: path and total cost
        """
        frontier = PriorityQueue()
        frontier.put((self.h[self.initial_location], self.initial_location))
        path = []
        cost = 0

        while frontier:
            current_cost, current = frontier.get()
            cost += current_cost
            path.append(current)


            if current == self.goal_location:
                break

            frontier = PriorityQueue()

            for i in self.graph[current]:
                if i[0] not in path:
                    frontier.put((self.h[i[0]], i[0]))
                    # print(self.h[i[0]], i[0])
        return path, cost


    def astar_search(self):
        """
        Performs search using - A* pathfinding algorithm, that uses
        f cost function = G cost (distance) + H cost (heuristics) on each
        possible route and calculates the route with lowest f cost amount
        :return: path and total cost
        """
        frontier = PriorityQueue()
        distance = 0
        path = []
        cost = 0

        frontier.put((self.h[self.initial_location] + distance, [self.initial_location, 0]))

        while frontier:
            current_cost, current = frontier.get()
            cost += current_cost

            path.append(current[0])
            distance += int(current[1])

            if current[0] == self.goal_location:
                break

            frontier = PriorityQueue()

            for i in self.graph[current[0]]:
                if i[0] not in path:
                    frontier.put((self.h[i[0]] + int(i[1]) + distance, i))
                    # print(self.h[i[0]] + int(i[1]) + distance, i)

        return path, cost
