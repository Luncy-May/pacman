# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

# from game import Directions
#     S = Directions.SOUTH
#     W = Directions.WEST
#     E = Directions.EAST
#     N = Directions.NORTH

def depthFirstSearch(problem):
    stack=util.Stack()
    visited=[]
    stack.push((problem.getStartState(),[]))
    visited.append(problem.getStartState())
    
    if problem.isGoalState(problem.getStartState()):
        return []
    
    while not stack.isEmpty():
        curr=stack.pop()

        for potentialnext in problem.getSuccessors(curr[0]):
            if potentialnext[0] not in visited:
                if problem.isGoalState(potentialnext[0]):
                    return curr[1]+[potentialnext[1]]
                
                else:
                    stack.push((potentialnext[0],(curr[1]+[potentialnext[1]])))
                    visited.append(potentialnext[0])
                
    return []

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    queue=util.Queue()
    visited=[]
    queue.push((problem.getStartState(),[]))
    visited.append(problem.getStartState())
    
    if problem.isGoalState(problem.getStartState()):
        return []
    
    while not queue.isEmpty():
        curr=queue.pop()

        for potentialnext in problem.getSuccessors(curr[0]):
            if potentialnext[0] not in visited:
                if problem.isGoalState(potentialnext[0]):
                    return curr[1]+[potentialnext[1]]
                
                else:
                    queue.push((potentialnext[0],(curr[1]+[potentialnext[1]])))
                    visited.append(potentialnext[0])
    return []

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    PQ = util.PriorityQueue()
    visited = []
    start = problem.getStartState()
    PQ.update((problem.getStartState(),[]), 0) # (item/tuple, cost)
    visited.append(problem.getStartState())
    if problem.isGoalState(problem.getStartState()):
        return []
    
    while not PQ.isEmpty():
        curr = PQ.pop()
        for potentialnext in problem.getSuccessors(curr[0]):
            nextPosition = potentialnext[0]
            nextDirection = potentialnext[1]
            nextCost = potentialnext[2]
            if potentialnext[0] not in visited:
                if problem.isGoalState(nextPosition):
                    return curr[1]+[nextDirection]
                else:
                    PQ.update((nextPosition,(curr[1]+[nextDirection])), problem.getCostOfActions(curr[1]+[nextDirection]))
                    visited.append(potentialnext[0])
        
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    PQ = util.PriorityQueue()
    visited = []
    start = problem.getStartState()
    PQ.update((problem.getStartState(),[]), 0) # (item/tuple, cost)
    visited.append(problem.getStartState())
    if problem.isGoalState(problem.getStartState()):
        return []
    
    while not PQ.isEmpty():
        curr = PQ.pop()
        for potentialnext in problem.getSuccessors(curr[0]):
            nextPosition = potentialnext[0]
            nextDirection = potentialnext[1]
            nextCost = potentialnext[2]
            if potentialnext[0] not in visited:
                if problem.isGoalState(nextPosition):
                    return curr[1]+[nextDirection]
                else:
                    PQ.update((nextPosition,(curr[1]+[nextDirection])), problem.getCostOfActions(curr[1]+[nextDirection]) + heuristic(curr[0], problem))
                    visited.append(potentialnext[0])
        
    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
