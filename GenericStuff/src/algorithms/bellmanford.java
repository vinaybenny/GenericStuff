package algorithms;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

import algorithms.shortestpathDAG.DirectedGraph;
import algorithms.shortestpathDAG.Edge;
import algorithms.shortestpathDAG.Node;

public class bellmanford {
	
	public class NegativeCycleException extends Exception{

		public NegativeCycleException(String string) {
			// TODO Auto-generated constructor stub
			System.out.println(string);
		}
	}
	
	// Implementation of Bellman-Ford algorithm for shortest-distance problem, with detection of negative cycles.
	// Complexity- O(V*E + E) = O(V*V*V)
	public <T> void bellfordalg(DirectedGraph<T> dg, Node<T> startingNode, 
			Set<Edge<T>> edges) throws NegativeCycleException{
		
		startingNode.distance = (double)0;
		
		// Iterate from 1 to V-1; and analyze every edge in each case. Complexity- O(V*E), V-> Vertices, E-> Edges
		for(int i=1; i <= dg.graph.size()-1; i++){
			for(Edge<T> edge : edges){
				
				if(edge.endingNode.distance > edge.startingNode.distance + edge.weight){
					edge.endingNode.distance = edge.startingNode.distance + edge.weight;
					edge.endingNode.previousnode = edge.startingNode;
				}				
			}
		}
		
		// Check for negative cycles to see if any edge can be further relaxed. Complexity- O(E).
		for(Edge<T> chkedge : edges){
			if(chkedge.endingNode.distance > chkedge.startingNode.distance + chkedge.weight){				
				throw new NegativeCycleException("The path has negative cycles in it. Aborting here.");
				
			}
		}
		
	}
	
	public static void main(String[] args){
		
		shortestpathDAG spd = new shortestpathDAG();
		Node<String> one = spd.new Node<String>("1");
		Node<String> two = spd.new Node<String>("2");
		Node<String> three = spd.new Node<String>("3");
		Node<String> four = spd.new Node<String>("4");
		Node<String> five = spd.new Node<String>("5");
		Node<String> six = spd.new Node<String>("6");
		
		//one.addEdge(three,2.0).addEdge(four,2.0);
		one.addEdge(four,-2.0);
		
		two.addEdge(four,1.0);
		three.addEdge(five,6.0);
		three.addEdge(one, 2.0);
		four.addEdge(three,-3.0).addEdge(five, 4.0);
		five.addEdge(six, -1.0);
		
		ArrayList<Node<String>> listofNodes = new ArrayList<Node<String>>();
		listofNodes.add(one);
		listofNodes.add(two);
		listofNodes.add(three);
		listofNodes.add(four);
		listofNodes.add(five);
		listofNodes.add(six);
		
		Set<Edge<String>> listofEdges = new HashSet<Edge<String>>();
		listofEdges.addAll(one.getoutgoingedges());
		listofEdges.addAll(two.getoutgoingedges());
		listofEdges.addAll(three.getoutgoingedges());
		listofEdges.addAll(four.getoutgoingedges());
		listofEdges.addAll(five.getoutgoingedges());
		
		DirectedGraph dg = spd.new DirectedGraph(listofNodes);
		bellmanford bf = new bellmanford();
		try {
			bf.bellfordalg(dg,five,listofEdges);
		} catch (NegativeCycleException e) {
			// TODO Auto-generated catch block			
			e.printStackTrace();
			return;
			
		}
		
		System.out.println("Distance of Node "+six.node+" from Node "+five.node+": "+six.distance);
		Node n = six;
		System.out.print("Node "+n.node);
		while(!n.node.equals(five.node)){
			System.out.print(" from ");
			System.out.print("Node "+n.previousnode.node);
			n= n.previousnode;
		}
	}
	
}
