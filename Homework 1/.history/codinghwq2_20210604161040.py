#Answers to Questions in the document can be found as comments in the main() function
import math
from search import Problem, breadth_first_search

class FlightState:
    #Part 1
    def __init__(self, city, time):
        self.current_city = city
        self.current_time = time
    
    def __repr__(self):
        return f'{self.current_city},{self.current_time}'

class Flight:
    def __init__(self, start_city, start_time, end_city, end_time):
        self.start_city = start_city
        self.start_time = start_time
        self.end_city = end_city
        self.end_time = end_time

    def __str__(self):
        return str((self.start_city, self.start_time))+ "->"+ str((self.end_city, self.end_time))

    def matches(self, city, time):
        #Part 2
        #returns boolean whether city and time match those of the flights, flight leaves city past the time argument
        return (self.start_city == city and self.start_time >= time)

flightDB = [Flight("Rome", 1, "Paris", 4),
            Flight("Rome", 3, "Madrid", 5),
            Flight("Rome", 5, "Istanbul", 10),
            Flight("Paris", 2, "London", 4),
            Flight("Paris", 5, "Oslo", 7),
            Flight("Paris", 5, "Istanbul", 9),
            Flight("Madrid", 7, "Rabat", 10),
            Flight("Madrid", 8, "London", 10),
            Flight("Istanbul", 10, "Constantinople", 10)]

class FlightProblem(Problem): #inheriting from Problem SuperClass
    def __init__(self, start, end):
        super().__init__(start, end) #start contains city and time, end contains city and time
        #calls the super class initialisation, sets initial state and goal state
    
    #implementing abstract methods
    def actions(self, state): #current flight state
        possible_actions = []
        for flight in flightDB:
            if flight.matches(state.current_city, state.current_time):
                possible_actions.append(flight)
        return possible_actions #returns a list of possible actions
    
    def result(self, state, action):
        return (FlightState(action.end_city, action.end_time)) #returns a new FlightState from carrying out the action

    def goal_test(self, state):
        return state.current_city == self.goal.current_city and state.current_time <= self.goal.current_time

#Part 3
def find_itinerary(start_city, start_time, end_city, deadline):
    start_flight_state = FlightState(start_city, start_time)
    end_flight_state = FlightState(end_city, deadline)
    flightProblem = FlightProblem(start_flight_state, end_flight_state)
    solution = breadth_first_search(flightProblem)
    return solution

def find_shortest_itinerary(start_city, end_city):
    #Part 4
    #When the shortest path is length 200, it will take roughly 2x number of calls to find_itinerary to solve
    #Assuming that a solution exist, it will always find the shortest path to the destination city
    start_time = 1
    deadline = 1
    solution = None
    while solution is None:
        solution = find_itinerary(start_city, start_time, end_city, deadline)
        deadline += 1

    shortest_itinerary = []
    for sol in solution.solution():
        shortest_itinerary.append(str(sol))

    return shortest_itinerary

def find_shortest_itienerary_challenge(start_city, end_city):
    #strategy runs in o(log(n)) with respect to find_itienrary_calls
    deadline = 1
    solution = None
    while solution == None:
        solution = find_itinerary('Rome', 1, 'Istanbul', deadline)
        if solution == None:
            deadline *= 2
    
    upperBound = solution.state.current_time
    lowerBound = deadline / 2

    while upperBound > lowerBound:
        middle = math.floor((upperBound + lowerBound)/2) #floor divide
        solution = find_itinerary('Rome', 1, 'Istanbul', middle)
        if solution == None:
            lowerBound = middle + 1
        else:
            upperBound = solution.state.current_time

    solution = find_itinerary('Rome', 1, 'Istanbul', upperBound)

    shortest_itinerary = []
    for sol in solution.solution():
        shortest_itinerary.append(str(sol))
    return shortest_itinerary

def main():
    '''
    Q2 - Part 1: Good Choice of State
    In this question, state is represented in the FlightState Class, and contains the attributes current time and current city

    '''
    #===========================================================================================================================
    '''
    Q2 - Part 1: State
    In this question, state is represented in the FlightState Class, and contains the attributes current time and current city

    '''

    #Part 4
    result = find_shortest_itinerary('Rome', 'Istanbul')
    #result = find_shortest_itienerary_challenge("Rome", "Istanbul")
    print (result)

if __name__ == "__main__":
    main()