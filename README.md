# Importance_equation
Computing the importance equations of all the nodes of a given graph having two disconnected components using **Google Page Ranking Algorithm**

####An example of edge connectivities of a connected component is given below.
  1 :2, 3, 4, 5
  2: 3, 1, 4
  3: 2, 4,
  4: 2

Assuming that a user jumps from node of one connected component to nodes of other component component with probability p, recomputing the importance equations after connecting the disconnected component with the given probability.

####Assumptions
1.Node number 1 is treated as alphabet 'a', 2 as 'b' so on till z.
2.No dangling nodes.

####Commands for executing the program
1.for help:python importance_equation.py --help
2.for execution: python importance_equation.py --f1 f1.txt --f2 f2.txt
where f1 and f2 are the input files containing graph details of first and second connected component respectively.
