
import numpy as np



def djstra(adj,start):
	print("djstra running...")
	adsize = len(adj)
	start_ = start
	dpmatrix = np.zeros(shape=(adsize+1,adsize))
	print(dpmatrix)
	for i in range(1,adsize):
		dpmatrix[i,start_] = dpmatrix[i-1,start_]
		adj_mark[i] = 0
		for j in range(1,adsize):
			if adj[i,j] and adj_mark[j]:
				if (dpmatrix[i-1,j] > dpmatrix[i,start_]+adj[i,j]):
					dpmatrix[i,j] = dpmatrix[i,start_]+adj[i,j]
				else:
					dpmatrix[i,j] = dpmatrix[i-1,j]



			








adj = np.array([[0,4,1],[4,0,2],[1,2,0]])
adj_dict = {}
adj_mark = {}
adj_dict[0] = np.array([[1,4],[2,1]])
adj_dict[1] = np.array([[0,4],[2,2]])
adj_dict[2] = np.array([[0,1],[1,2]])
adj_mark[0] = adj_mark[1] = adj_mark[2] = 1

djstra(adj,0)



