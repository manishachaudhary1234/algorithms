class UnionFind():
	
	def __init__(self, edges):
		self.node_to_leader = {}
		self.leader_to_size = {}
		self.num_leaders = 0
	
		for edge in edges:
			if edge[0] not in self.node_to_leader:
				self.node_to_leader[edge[0]] = edge[0]
				self.leader_to_size[edge[0]] = 1
				self.num_leaders += 1
			if edge[1] not in self.node_to_leader:
				self.node_to_leader[edge[1]] = edge[1]
				self.leader_to_size[edge[1]] = 1
				self.num_leaders += 1

	def get_leader(self, node):
		return self.node_to_leader[node]

	def have_same_leader(self, node1, node2):
		if self.get_leader(node1) == self.get_leader(node2):
			return True
		else:
			return False
	
	# merges groups that those two nodes belong to
	def merge(self, node1, node2):
		if self.leader_to_size[node1] > self.leader_to_size[node2]:
			old_leader = self.get_leader(node2)
			new_leader = self.get_leader(node1)

		else:
			old_leader = self.get_leader(node1)
			new_leader = self.get_leader(node2)

		for key in self.node_to_leader:
			if self.node_to_leader[key] == old_leader:
				self.node_to_leader[key] = new_leader
				self.leader_to_size[old_leader] -= 1
				self.leader_to_size[new_leader] += 1

		self.num_leaders -= 1



def num_from_bits(bits, bits_per_node):
	num = 0
	for i in range(0, bits_per_node):
		exponent = bits_per_node - i - 1
		num += int(bits[i]) * 2**exponent
	
	return num


#(1) Read file
f = open('clustering_big.txt', 'r')
#f = open('clustering_big_T1.txt', 'r')
#f = open('clustering_big_T2.txt', 'r')
lines = f.readlines()
f.close()

num_nodes, bits_per_node = lines[0].split(' ')
num_nodes, bits_per_node = int(num_nodes), int(bits_per_node)


nodes = {}
nodes_frequency = {}
nodes_arr = []
for line in lines[1:]:
	bits = line.split(' ')
	if bits[-1] == "\n":
		bits.pop(-1)
	elif '\n' in bits[-1]:
		bits[-1] = bits[-1].split('\n')[0]

	#sanity
	assert len(bits) == bits_per_node, "The given bits per node at the beginning of the file %d doesn't match the actual %d bits per node" % (bits_per_node, len(bits))

	#construct an unsigned integer out of the bits
	num = num_from_bits(bits, bits_per_node)

	nodes[num] = bits
	nodes_arr.append(num)
	if num in nodes_frequency:
		nodes_frequency[num] += 1
	else:
		nodes_frequency[num] = 1



edges = []
for num in nodes:
	# 0 bit hamming difference 
	cost = 0
	bits = nodes[num]

	if nodes_frequency[num] > 1:
		for i in range(0, nodes_frequency[num] - 1):
			# need to find a different identity for second node (otherwise will be interpreted as the same node)
			edge = [num, num + num_nodes + i, cost]
			edges.append(edge)


print edges
		
# Do the 1 bit difference after the 0 bit difference to keep the edges sorted
for num in nodes:
	# 1 bit hamming difference ( 24 possible nodes)
	cost = 1
	bits = nodes[num]

	for i in range(0, bits_per_node):
		new_bits = bits[:]
		if bits[i] == '1':
			new_bits[i] = '0'
		else:
			new_bits[i] = '1'
	
	new_num = num_from_bits(new_bits, bits_per_node)

	if new_num in nodes:
		edge = [num, new_num, cost]
		if [new_num, num, cost] not in edges:
			edges.append(edge)

print edges

# Do the 2 bits difference after the 1 bit difference to keep the edges sorted
for num in nodes:
	# 2 bits hamming difference ( 24 * 23 / 2 possible nodes)
	cost = 2
	bits = nodes[num]

	for i in range(0, bits_per_node):
		new_bits = bits[:]
	
		if bits[i] == '1':
			new_bits[i] = '0'
		else:
			new_bits[i] = '1'
		
		for j in range(i + 1, bits_per_node):
			if bits[j] == '1':
				new_bits[j] = '0'
			else:
				new_bits[j] = '1'

			new_num = num_from_bits(new_bits, bits_per_node)
	
			if new_num in nodes:
				edge = [num, new_num, cost]
				if [new_num, num, cost] not in edges:
					edges.append(edge)
			# Must reflip the bits before next iteration!
			else:
				if new_bits[j] == '0':
					new_bits[j] = '1'
				else:
					new_bits[j] = '0'

print edges

# build union find
union = UnionFind(edges)

# run the algorithm
clusters = num_nodes
for edge in edges:
	if not union.have_same_leader(edge[0], edge[1]):
		union.merge(edge[0], edge[1])
		clusters -= 1

print clusters	
