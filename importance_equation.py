#!/usr/bin/python

import string
import sys
import argparse

def build_dictionary(filename,intra_prob=0.8):
	'''returns a dictionary where key is the node number and value is all incoming node with importance value'''

	nodes=[]
	dictnry={}
	for line in filename:
		
		from_node,to_nodes=line.split(":")
		from_node=from_node.strip()
		nodes.append(from_node)
		
		to_nodes=to_nodes.strip()
		to_nodes=to_nodes.split(",")
		
		#caluclating denominator
		out_degree=float(len(to_nodes)) 
		edge_value=intra_prob/out_degree
		for key in to_nodes:
			# key is node name and values are indegree of (denominator times node value)
			dictnry.setdefault(key, []) 
			dictnry[key].append((edge_value,from_node))
	
	filename.close()
	return nodes,dictnry
 
def connect_components(comp1, comp2, comp2_dict, inter_prob=0.2):
	'''connects two disconnected components with given probabilities and returns dictionary'''
	
	edge_value=inter_prob/len(comp2)
	for key in set(comp2):
		for node in comp1:
			comp2_dict.setdefault(key, []).append((edge_value,node))   

def print_importance_equation(comp_dictionary):
	'''given the dictionary of a component, prints the importance equation for all the nodes in that component
	   ex: 3:[(0.8/3 , 2),(0.8 , 1)] then, importance equation would be c=0.2666666 * b + 0.8 * a'''
	
	#mapping numbers to alphabets ex: 1:a 2:b.......26:z
	dic=dict(zip(range(1,27),string.ascii_lowercase))

	for key,value in comp_dictionary.items():
		equation=dic[int(key)]+" = "
		count=0
		
		for a,b in value:
			if count!=0:
				equation=equation+" + "+str(a)+" * "+dic[int(b)]
			else:
				equation=equation+str(a)+" * "+dic[int(b)]
				count=5
					
		print equation

	

if __name__ == "__main__":
	
	parser=argparse.ArgumentParser();
	parser.add_argument("--f1",help="File containing the node component 1",required=True)
	parser.add_argument("--f2",help="File containing the node component 2",required=True)
	args=parser.parse_args()

	file1=args.f1
	file2=args.f2

	try:
		fp1=open(file1)
		fp2=open(file2)
	except:
		print("file not found")
		sys.exit(0)

	comp1_nodes, comp1_dictionary=build_dictionary(fp1)
	comp2_nodes, comp2_dictionary=build_dictionary(fp2)

	#connecting two disconnected components(comp1 and comp2) with given inter probability
	connect_components(comp1_nodes, comp2_nodes, comp2_dictionary, inter_prob=0.2)
	connect_components(comp2_nodes, comp1_nodes, comp1_dictionary, inter_prob=0.2)

	print_importance_equation(comp1_dictionary)
	print_importance_equation(comp2_dictionary)
	
