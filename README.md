##Importance_equation
Computing the importance equations of all the nodes of a given graph having two disconnected components using **Google Page Ranking Algorithm**

**An example of edge connectivities of a connected component is given below.**</br>
  1 :2, 3, 4, 5</br>
  2: 3, 1, 4</br>
  3: 2, 4</br>
  4: 2</br>

Assuming that a user jumps from node of one connected component to nodes of other component component with probability p, recomputing the importance equations after connecting the disconnected component with the given probability.

**Assumptions**</br>
1.Node number 1 is treated as alphabet 'a', 2 as 'b' so on till z.</br>
2.No dangling nodes.</br>

**Commands for executing the program**</br>
1.for help:**python importance_equation.py --help**</br>
2.for execution: **python importance_equation.py --f1 f1.txt --f2 f2.txt**</br>
where f1 and f2 are the input files containing graph details of first and second connected component respectively.</br>

**Sample Input:**</br>
f1.txt(component1)</br>
1:2</br>
2:3</br>
3:2,1</br>

f2.txt(component2)</br>
4:5</br>
5:6</br>

**Sample output:**</br>
e = 0.8 * d + 0.1 * a + 0.1 * b + 0.1 * c</br>
d = 0.8 * e + 0.1 * a + 0.1 * b + 0.1 * c</br>
a = 0.4 * c + 0.0666666666667 * d + 0.0666666666667 * e</br>
c = 0.8 * b + 0.0666666666667 * d + 0.0666666666667 * e</br>
b = 0.8 * a + 0.4 * c + 0.0666666666667 * d + 0.0666666666667 * e</br>
