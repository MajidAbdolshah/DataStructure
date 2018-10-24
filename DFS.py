
def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

def path_dfs(graph,start,end):
	stack = [(start,[start])]
	while stack:
		(vertex,path) = stack.pop()
		for next in graph[vertex] - set(path):
			if next == end:
				yield path+[next]
			else:
				stack.append((next,path + [next]))
def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

print(list(path_dfs(graph, 'A', 'F')))
print(list(bfs_paths(graph, 'A', 'F')))