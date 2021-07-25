def createGraph(projects, dependencies):
    projectGraph = {}
    for project in projects:
        projectGraph[project] = []
    for pairs in dependencies:
        projectGraph[pairs[0]].append(pairs[1])
    return projectGraph

def getProjectWithDependancy(projectGraph):
    projectWithDependancies = set()
    for project in projectGraph:
        projectWithDependancies = projectWithDependancies.union(set(projectGraph[project]))
    return projectWithDependancies

def getProjectWithoutDependancy(projectGraph,projectWithDependancies):
    getProjectWithoutDependancy = set()
    for project in projectGraph:
        if(project not in projectWithDependancies):
            getProjectWithoutDependancy.add(project)
    return getProjectWithoutDependancy

def findBuildOrder(projects,dependencies):
    buildOrder = []
    projectGraph = createGraph(projects,dependencies)
    while projectGraph:
        projectWithDependancies = getProjectWithDependancy(projectGraph)
        projectWithoutDependancies = getProjectWithoutDependancy(projectGraph,projectWithDependancies)
        for project in projectWithoutDependancies:
           buildOrder.append(project)
           del projectGraph[project]       

    return buildOrder 

projects = ['a', 'b', 'c', 'd', 'e', 'f']
dependencies = [('a','d'), ('f','b'), ('b','d'), ('f','a'), ('d','c')]

print(findBuildOrder(projects,dependencies))
