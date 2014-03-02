package algorithms;

import java.util.HashMap;

public class knapsackproblem {
	
	private static int callcount = 0;
	
	//Simple recursive binary tree traversal, leftmost first, Brute force method
	public static int maxValue(int[] weights, int[] values, int maxweight, int index){		
		
		callcount++;
		System.out.println("maxValue called with index: "+index+", remaining weight: "+maxweight);
		int without_i=0, with_i=0;
		if(index == 0){
			if(weights[0] <= maxweight)
				return values[0];
			else 
				return 0;
		}
		
		else {
			//Left subtree
			without_i = maxValue(weights, values, maxweight, index-1);
			
			//Right subtree
			if(weights[index] <= maxweight){
				with_i = values[index] + maxValue(weights, values, maxweight - weights[index], index-1);
				
			}
			
			return Math.max(without_i, with_i);
		}
	}
	
	public static int fastmaxvalue(int[] weights, int[] values, int maxweight, int index, HashMap< HashMap<Integer, Integer>,Integer>  memo){
		callcount++;
		System.out.println("maxValue called with index: "+index+", remaining weight: "+maxweight);
		int without_i=0, with_i=0;
		
		HashMap<Integer, Integer> pair = new HashMap<Integer,Integer>();
		pair.put(index, maxweight);
		
		if(memo.containsKey(pair)){
			return memo.get(pair);
		}
		
		else{
			
			if(index == 0){
				if(weights[0] <= maxweight){
					memo.put(pair, values[0]);
					return values[0];
				}
				else{ 
					memo.put(pair, 0);
					return 0;
				}
			}			
			else {
				//Left subtree
				without_i = fastmaxvalue(weights, values, maxweight, index-1, memo);
				
				//Right subtree
				if(weights[index] <= maxweight){
					with_i = values[index] + fastmaxvalue(weights, values, maxweight - weights[index], index-1, memo);
					
				}
				memo.put(pair, Math.max(without_i, with_i));
				return Math.max(without_i, with_i);
			}
		}
	}
	
	private static boolean matchkey(HashMap<Integer, Integer> pair, HashMap<HashMap<Integer, Integer>, Integer> memo) {
		// TODO Auto-generated method stub
		
		System.out.println("Inside matchkey: "+pair.keySet().toArray()[0]);
		
		for( HashMap key : memo.keySet()){
			
			if(true){
				
				if(key.get(pair.keySet().toArray()[0]) == pair.values().toArray()[0])
					return true;
				
			}
		}
		
		return false;
	}

	public static void main(String[] args){
		
//		int[] weights = {1,5,3,4,1,5,3,4};
//		int[] values = {15,10,9,5,15,10,9,5};
		int[] weights = {1,1,5,5,3,3,4,4};
		int[] values = {15,15,10,10,9,9,5,5};
		int maxweight = 8;
		int index = weights.length - 1, maxval;
		
//		maxval = maxValue(weights, values, maxweight, index);
//		System.out.println("Maximum value possible in this problem is: "+ maxval + " and callcount is: "+callcount);
		
		callcount=0; maxval=0;
		HashMap< HashMap<Integer, Integer>,Integer>  memo = new HashMap< HashMap<Integer, Integer>,Integer>();
		maxval = fastmaxvalue(weights, values, maxweight, index, memo);
		System.out.println("Maximum value possible in this problem is: "+ maxval + " and callcount is: "+callcount);
	}

}
