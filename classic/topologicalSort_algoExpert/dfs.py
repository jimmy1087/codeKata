def topologicalSort(jobs, deps):
    jobGraph = createJobGraph(jobs, deps)   # 1 Create Graph
    return getOrderedJobs(jobGraph)  # Solve sorting by DFS

def createJobGraph(jobs, deps):
    graph = JobGraph(jobs)   # Fill graph vertices
    for prereq, job in deps: # Add Edges to the Graph
        graph.addPrereq(job, prereq)
    return graph

def getOrderedJobs(graph):
    orderedJobs = []
    nodes = graph.nodes
    while nodes:
        node = nodes.pop() # Iterate over JobNodes ONCE even if they are disconnected
        containsCycle = traverseDFS(node, orderedJobs) # Handles cycle + DFS
        if containsCycle:
            return []
    return orderedJobs

def traverseDFS(node, orderedJobs):  # Works at JobNode level, using status + navigation between dependencies
    if node.visited:
        return False
    if node.visiting:
        return True
    node.visiting = True
    for prereqNode in node.prereqs:
        containsCycle = traverseDFS(prereqNode, orderedJobs)
        if containsCycle:
            return True
    node.visited = True
    node.visiting = False
    orderedJobs.append(node.job) # Reaching the last prereq, we can now safely add this JobNode to the ordered list.

class JobGraph:

    def __init__(self, jobs):
        self.nodes = []    # Optional, but it allow us to iterate thru nodes very easily
        self.graph = {}
        for job in jobs:
            self.addNode(job)

    def addNode(self, job):
        self.graph[job] = JobNode(job)
        self.nodes.append(self.graph[job])

    def addPrereq(self, job, prereq):  
        jobNode = self.getNode(job)       # From indexes or Job Names, obtain JobNode object
        prereqNode = self.getNode(prereq)
        jobNode.prereqs.append(prereqNode)

    def getNode(self, job):
        if job not in self.graph:
            self.addNode(job)
        return self.graph[job]    # Constant time access

class JobNode:

    def __init__(self, job):
        self.job = job
        self.prereqs = [] # Graph portion of the Alg. Used to traverse connected nodes
        self.visited = False
        self.visiting = False


############################### Tests
#Dependency:  (Prerequirement, Job)


'''
    A -* B
    |   **
    |  / |
    * /  |
    C *- D
'''
jobs = ['A', 'B', 'C', 'D']
deps = [['A','B'], ['A','C'],['C','B'],['D','B'],['D','C']]
#assert ( ['A','D','C','B'] or ['D','A','C','B'] ) 
print(topologicalSort(jobs, deps))