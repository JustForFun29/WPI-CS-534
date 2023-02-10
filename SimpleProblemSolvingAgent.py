'''
***
1) Implement a SimpleProblemSolvingAgent (SPSA) class that you can use to instantiate
a SPSA object to find the best path between any two Romania cities.

2) For the SPSA class, you need to develop and implement two informed searching algorithms:
Greedy Best-First Search (i.e., best_first_graph_search (problem, f) and
A* Search (i.e., astar_search(problem, h).

3) THe SPSA object will take a graph, i.e., the Romania map, as an input shown in Figure 3.1
of your textbook and the city coordinates, and any two cities in the map to find the best
path between them using both Greedy Best-First Search and A* Search algorithms, respectively.
THe map file implementation should include the (romania_map) and (romania_map.locations) that
I have shown you in my lecture slide and video as the reference and the starting point.

4) Develop and implement a separate python App program called (RomaniaCityApp.py) using the
given construct and do the following:
(a) Your app will prompt and ask for a user to enter where the map file is located in your
 local directory and then read the (romania_map) and (romania_map.locations) in the map file.
 You can store your map file in any file type that you prefer only if your app can access the
 map file and read the (romania_map) and (romania_map.locations) in the map file.
 (b) Your app will then prompt and ask for a user to enter any two cities from the (romania_map).
 If these two cities are the same or either one of them or both of them cannot be found in the
 Romania map, please ask for the user to enter them again until the two cities are valid.
 (c)  Your app will then create a SPSA object from the (SimpleProblemSolvingAgent) class and
 search the best path between these two cities by using the Greedy Best-First Search and A*
 Search algorithms, respectively.  For each search alogorithm used, the output should include
 (i) the search method name, (ii) the total cost of the path, and the difference between these two
 search alogorithms.
 (d) At the end, your app will ask for theuser if they would like to find the best path between
 any two cities again.  If yes, repeat (b) and (c).  If no, terminate the program and then display
 "Thank You for Using Our App".


'''

class SimpleProblemSolvingAgentProgram:
    '''
    Section 3.1 & 3.2 - Textbook
    '''

    def __init__(self, initial_state=None):
        '''State is an abstrace representation of the state of the world,
        and seq is the list of actions required to get to a particular
        state from the inital state(root).'''
        self.state = initial_state
        self.seq = []

    def __call__(self, percept):
        '''Figure 3.1 - Formulate a goal and problem, them search for a
        sequence of actions to solve it.'''
        self.state = self.update_state(self.state, percept)
        if not self.seq:
            goal = self.formulate_goal(self.state)
            problem = self.formulate_problem(self.state, goal)
            self.seq = self.search(problem)
            if not self.seq:
                return None
        return self.seq.pop(0)

    def update_state(selfself, state, percept):
        raise NotImplemented

    def formulate_goal(selfself, state):
        raise NotImplemented

    def formulate_problem(self, state, goal):
        raise NotImplemented

    def search(selfself, problem):
        raise NotImplemented

