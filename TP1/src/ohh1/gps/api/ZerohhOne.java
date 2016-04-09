package ohh1.gps.api;

import gps.SearchStrategy;

public class ZerohhOne {

	private static Ohh1Engine engine;
	
	public static void main(String[] args){
		engine = new Ohh1Engine();
		
		System.out.println("0hh1 Start!");
		try{
			engine.engine(new Ohh1Problem(), SearchStrategy.DFS);
		} catch(Exception e) {
			System.out.println("Solution (if any) too deep for stack");
		}
		System.out.println("0hh1 Finish!");
	}
}
