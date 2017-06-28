
import csv as csv
import random as random
import copy as copy



def minCut(G,E):

	Q = copy.deepcopy(G);
	
	s = random.sample(E,1);
	u = s[0][0]
	v = s[0][1]
	# rebinding list
	_E = [(i, j) for i, j in E if i!=u and j!=v]
	
	keys = Q.keys();
	# kind of like union find
	# list of each vertex and its cluster leader
	C = {}

	while len(keys) >2:
		#print "keys"+str(keys)
		# merge u and v
		# merge always to u
		print "merging "+str(u)+" "+str(v)
		uEdges = Q[u]
		vEdges = Q[v]
		edges = vEdges + uEdges
		del Q[v]
		#assign leaders
		C[u] =u
		C[v] =u
		# now see if anyone had "v" as a leader, change to u
		for k in C.keys():
			if C[k] == v:
				C[k] = u
		
		# go through the edges of u
		# and find the ones that are on the same cluster 
		# i.e. u is the leader
		# and remove them
		_edges = copy.deepcopy(edges);
		for e in edges:
			if C.get(e)!=None and C[e] == u:
				#print "removing edge"+str(e)
				_edges.remove(e)
		edges = _edges
		Q[u] = edges
		
		#print Q	
		#print "union find"
		#print C

		#now select new u, v 
		# if we have more than 2 vertexes in our keys
		keys = Q.keys()
		if len(keys) ==2:
			#we are done
			#print Q
			break
		_vertex = v
		while _vertex==v:
			s = random.sample(_E,1);
			#print "u"+str(u)
			_u = s[0][0]
			_v = s[0][1]
			# when picking cases
			# never contracted before, if contracted get their leaders from C 
			print "_u and _v"+str(_u)+" "+str(_v)
			if C.get(_v)==None:
				v = _v
			if C.get(_u)==None:
				u = _u
			if C.get(_v) != C.get(_u):
				if C.get(_u)!=None:
					u =C[_u]
				if C.get(_v)!=None:
					v = C[_v]

			# the case C.get(_v) == C.get(_u) 
			# is the one in which both vertexes have already been merged
			# remove them from edge list try again
			# rebinding list
			_E = [(i, j) for i, j in E if i!=_u and j!=_v]

	minCutNumberOfVertexes = len(Q[keys[0]]) 
	print ">>>local min"+str(minCutNumberOfVertexes);
	return minCutNumberOfVertexes 

f = open('./kargerMinCut.txt');
reader = csv.reader(f,delimiter='\t', quoting=csv.QUOTE_NONE)
#f = open('./testCase3.txt');
#reader = csv.reader(f,delimiter=' ', quoting=csv.QUOTE_NONE)

G = {}
V = 0
E =[]; #tuples of edges to pick an edge at random
for row in reader:
	V = V+1
	v = int(row[0])
	tails = [] # not set as later this structure will hold repeated edges to one vertex
	l = len(row)
	for i in range(1,l):
		w = row[i]
		if w.isdigit():
			w = int(w)
			tails.append(w)
			t = (v,w);
			E.append(t);
	G[v] = tails

#print E

# now we need to start contracting graph
keys = G.keys();

#print G

minCutNumberOfVertexes = 1000;

counter = 10;

print "Minimum found in "+str(counter)+" attempts "

while counter>0:
	seed = random.sample(keys,1);
	seed = seed[0]
	minCutNumber = minCut(G,E)
	#print minCutNumber
	minCutNumberOfVertexes = min(minCutNumberOfVertexes,minCutNumber)
	counter = counter-1

print "Final min:"
print minCutNumberOfVertexes