from pathlib import Path
from GroupProject01.SimpleProblemSolvingAgent import SimpleProblemSolvingAgent

def main():
    while True:
        graph_file_name = input("Please enter the name of the file where romania map is located: ")
        locations_file_name = input("Please enter the name of the file where coordinates of romania cities are located: ")

        file1 = Path('./'+graph_file_name)
        file2 = Path('./'+locations_file_name)

        if graph_file_name == locations_file_name or not file1.is_file() or not file2.is_file():
            print("Something went wrong! Either you provided same file names or there is no txt files with given names")
            continue

        while True:
            initial_city = input("Please enter the name of the starting destination: ").capitalize()
            goal_city = input("Please enter the name of the goal destination: ").capitalize()

            if initial_city == goal_city:
                print("You cannot enter same cities as a starting and goal destinations!")
                continue

            spsa = SimpleProblemSolvingAgent(graph_file_name, locations_file_name, initial_city, goal_city)

            if not spsa.city_validator():
                print("City names that you entered are either not in the romania map file or coordinates file. Try again")
                continue


            bfs_path, bfs_cost = spsa.best_first_graph_search()
            print("Performing Best First Graph Search")
            print("Found path: ", bfs_path)
            print("Total cost: ", bfs_cost)

            astar_path, astar_cost = spsa.astar_search()
            print("Performing A* Search")
            print("Found path: ", astar_path)
            print("Total cost: ", astar_cost)

            again = input("Would you like to try again? Yes/No: ").capitalize()

            if again == "Yes":
                continue
            else:
                print("Thank You For Using Our App")
                break


        break



if __name__ == '__main__':
    main()