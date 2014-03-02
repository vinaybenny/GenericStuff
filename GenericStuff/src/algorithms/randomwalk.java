package algorithms;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class randomwalk {

	private class negativeTimeException extends Exception{
		
	}
	private class Pair<X,Y> {
		private X elem1; 
		private Y elem2;
		
		private Pair(X x, Y y){
			this.elem1 = x;
			this.elem2 = y;
		}
	}
	
	private class Position{
		private double xcoord, ycoord;
		private Position(){
			this.xcoord = (double)0;
			this.ycoord = (double)0;
		}
		private Position(double xcoord, double ycoord){
			this.xcoord = (double)xcoord;
			this.ycoord = (double)ycoord;
		}
		private void setposition(double xcoord, double ycoord){
			this.xcoord = xcoord;
			this.ycoord = ycoord;
		}
		private Pair<Double, Double> getposition(){
			return new Pair(this.xcoord, this.ycoord);
		}		
	}
	
	private class Direction{
		private final List<String> possibledirs = new ArrayList<String>(){{
			add("N"); add("S"); add("E"); add("W");
		}};
		private Position onestep(){
			Random randomgenerator = new Random();
			int index = randomgenerator.nextInt(possibledirs.size());
			String direction = possibledirs.get(index);
			
			switch(direction){
			case "N": return new Position(0.0,1.0);
			case "S": return new Position(0.0,-1.0);
			case "E": return new Position(-1.0,0.0);
			case "W": return new Position(1.0,0.0);
			default: return new Position(0.0,0.0);
			}
		}
			
	}
	
	public class Drunk{
		private String name;
		private double distance;
		private Position currentposition;
		private Direction nextdirection;
		
		public Drunk(){
			this.distance = (double)0;
			this.currentposition = new Position();
			this.nextdirection = new Direction();
		}
		private void setname(String name){
			this.name = name;
		}
		private String getname(){
			return this.name;
		}
		
		private double[][] performSimulation(int time, int numtrials){
			
			double[][] simdata = new double[numtrials][time+1];
			try{
				if(time <= 0 ){
					throw new negativeTimeException();
				}
				
				for(int i = 0; i < numtrials; i++){
					this.currentposition.xcoord = 0.0;
					this.currentposition.ycoord = 0.0;
					double[] x = performtrials(time);
					simdata[i] = x;
				}
				return simdata;
				
			}catch(negativeTimeException negtime){
				System.out.println("Invalid Time");
				return simdata;
			}
			catch(Exception x){
				System.out.println("Code Failure in performSimulation");
				return simdata;				
			}		
		}
		
		private double[] performtrials(int time) {
			
			double[] distances = new double[time+1];
			distances[0]=0.0;
			for(int i = 1; i <= time; i++ ){
				distances[i] = this.move();
			}
			return distances;
						
		}
		private double move() {
			// TODO Auto-generated method stub
			Position pstn = this.nextdirection.onestep();
			this.currentposition.xcoord += pstn.xcoord;
			this.currentposition.ycoord += pstn.ycoord;
			double dist = Math.pow( Math.pow(this.currentposition.xcoord, 2) + Math.pow(this.currentposition.ycoord, 2), 0.5 );
			return dist;
		}
	}
	
	public static void main(String[] args){
		randomwalk r = new randomwalk();
		Drunk drunk = r.new Drunk();
		
		drunk.setname("Homer Simpson");
		
		double[][] output = drunk.performSimulation(100, 4);
		
		return;
		
	}
}
