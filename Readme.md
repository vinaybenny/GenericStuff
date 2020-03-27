# GenericStuff
This repository is intended to be a collection of Java/Python based implementations for well known algorithms for learning purposes only. My own implementations, and not intended for public use.

## List of files
1. dynamicfibonacci- recursive dynamic programming implementation for fibonacci series.
2. knapsackproblem- recursive dynamic programming implementation and naive recursive implementation 
   for knapsack problem with value and weight.
3. nrootfinder- recursive implementation of root finding using Newton-Raphson method.
4. randomwalk- simple implementation of the random walk simulation.
5. shortestpathDAG - implements the shortest path algorithm for a directed acyclic graph with 
   complexity of O(V+E); V->Vertices and E-> Edges. Also has an implementation of the topological sort 
   algorithm for DAGs, involving a recursive depth-first search method.
6. dijkstrasalgorithm- Two implementations of the Dijkstra's algorithm, using priority queue 
   Order -> O(V log(V)+ E log(V) ) and the faster fibonacci heap. This code is dependent on shortestpathDAG 
   for the directed graph class.
7. bellmanford- Implementation of Bellman-Ford shortest path algorithm, with detection of negative cycles.
   Complexity of O(V*E + E) -> O(Vcubed).dependent on shortestpathDAG for the directed graph class.
8. insertion_and_merge_sort- Implementation of Insertion sort, both recursive and non-recursive. The implementation
	also contains a binary seach based insertion sort. Complexity of O(n^2)
	There is also an implementation of recursive merge sort in this code, with a complexity of o(n*log(n)).
9. heap_sort_recursive- Implementation of a Node, Graph and Heap data structures. This is followed by an
	implementation of Heap sort. Complexity of O(n*log(n)).
