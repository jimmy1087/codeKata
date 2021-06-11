def topologicalSort(jobs, deps):
    jobGraph = createJobGraph(jobs, deps)
    return getOrderedJobs(jobGraph)

def createJobGraph(jobs, deps):
    graph = JobGraph(jobs)
    for job, dep in deps:
        graph.addDependency(job, dep)
    return graph

def getOrderedJobs(graph):
    orderedJobs = []
    nodesWithNoPrereq = list(filter(lambda node: node.numPreReqs == 0, graph.nodes))
    while nodesWithNoPrereq:
        node = nodesWithNoPrereq.pop()
        orderedJobs.append(node.job)
        removeDependencies(node, nodesWithNoPrereq)
    graphHasEdges = any(node.numPreReqs for node in graph.nodes)
    return [] if graphHasEdges else orderedJobs

def removeDependencies(node, nodesWithNoPrereq):
    while node.dependencies:
        dep = node.dependencies.pop()
        dep.numPreReqs -= 1
        if dep.numPreReqs == 0:
            nodesWithNoPrereq.append(dep)

class JobGraph:

    def __init__(self, jobs):
        self.nodes = []
        self.graph = {}
        for job in jobs:
            self.addNode(job)

    def addNode(self, job):
        self.graph[job] = JobNode(job)
        self.nodes.append(self.graph[job])

    def addDependency(self, job, dep):
        jobNode = self.getNode(job)
        depNode = self.getNode(dep)
        jobNode.dependencies.append(depNode)
        depNode.numPreReqs += 1

    def getNode(self, job):
        if job not in self.graph:
            self.addNode(job)
        return self.graph[job]

class JobNode:

    def __init__(self, job):
        self.job = job
        self.dependencies = []
        self.numPreReqs = 0



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