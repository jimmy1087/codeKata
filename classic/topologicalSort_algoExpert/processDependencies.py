def topologicalSort(jobs, deps):
    jobGraph = createJobGraph(jobs, deps)
    return getOrderedJobs(jobGraph)

def createJobGraph(jobs, deps):
    graph = JobGraph(jobs)
    for prereq, job in deps:
        graph.addPrereq(job, prereq)
    return graph

def getOrderedJobs(graph):
    orderedJobs = []
    while graph.nodesNoReq:
        nodeNoReq = graph.nodesNoReq.pop()
        graph.removeDependencies(nodeNoReq)
        orderedJobs.append(nodeNoReq.job)
    return orderedJobs

class JobGraph:

    def __init__(self, jobs):
        self.nodes = []
        self.nodesNoReq = []
        self.graph = {}
        for job in jobs:
            self.addNode(job)

    def addNode(self, job):
        self.graph[job] = JobNode(job)
        self.nodes.append(self.graph[job])
        self.nodesNoReq.append(self.graph[job])

    def addPrereq(self, job, prereq):
        jobNode = self.getNode(job)
        prereqNode = self.getNode(prereq)
        jobNode.prereqs.append(prereqNode)
        jobNode.depNum += 1
        if jobNode in self.nodesNoReq:
            self.nodesNoReq.remove(jobNode)

    def removeDependencies(self, dep):
        for node in self.nodes:
            if dep in node.prereqs:
                node.prereqs.remove(dep)
                node.depNum -= 1
                if node.depNum == 0:
                    self.nodesNoReq.append(node)

    def getNode(self, job):
        if job not in self.graph:
            self.addNode(job)
        return self.graph[job]

class JobNode:

    def __init__(self, job):
        self.job = job
        self.depNum = 0
        self.prereqs = []


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