package ohh1.solver;

import gps.GPSEngine;
import gps.SearchStrategy;
import gps.api.GPSProblem;
import ohh1.gps.api.Ohh1Engine;
import ohh1.gps.api.Ohh1Problem;
import ohh1.gps.api.Ohh1State;

public class Ohh1Solver {

	public static void main(String[] args) {
		
		/*
		 * Arguments
		 * 1. Heuristic
		 * 2. Search strategy
		 * 3. Board size
		 * 
		 */
		
		if(args.length == 3){
			try{
				int boardSize = Integer.parseInt(args[2]);
				
				if(boardSize == 4 || boardSize == 6 || boardSize == 8){
					Ohh1State.setSize(boardSize);
					System.out.println("Game board size: " + boardSize + "x" + boardSize);
				} else {
					System.out.println("Invalid size! Size must be '4', '6' or '8'");
					return;
				}
				
			}catch(NumberFormatException ex){
				System.out.println("Invalid arguments! Size must be a number");
				return;
			}
		} else {
			System.out.println("Invalid arguments!");
			System.out.println("Arguments must be (in order) : Heuristic, Search strategy, Board size");
			System.out.println("Heuristics available: SwapsPerRows, SwapsPerCols");
			System.out.println("Search strategies available: IDDFS, BFS, DFS, ASTAR, GREEDY");
			System.out.println("Boards of size 4, 6 or 8 only");
			return;
		}
		
		String heuristic = args[0];
		
		if(heuristic.equalsIgnoreCase("swapsperrow")){
			//TODO : Seleccionar el enum que corresponda a esta heuristica			
		} else if( heuristic.equalsIgnoreCase("swapspercol")){
			//TODO : Idem a arriba
		} else {
			System.out.println("Invalid arguments! Heuristics must be 'SwapsPerRow' or 'SwapsPerCol'");
			return;
		}
		
		GPSProblem ohh1Problem = new Ohh1Problem();
		GPSEngine solver = new Ohh1Engine();
		
		String searchStrategy = args[1];
		
		if(searchStrategy.equalsIgnoreCase(SearchStrategy.IDDFS.toString())){
			System.out.println("Starting engine with search strategy: " + "Iterative");
			solver.engine(ohh1Problem, SearchStrategy.IDDFS);
		}
		
		if(searchStrategy.equalsIgnoreCase(SearchStrategy.BFS.toString())){
			System.out.println("Starting engine with search strategy: " + "BFS");
			solver.engine(ohh1Problem, SearchStrategy.BFS);
		}
		
		if(searchStrategy.equalsIgnoreCase(SearchStrategy.DFS.toString())){
			System.out.println("Starting engine with search strategy: " + "DFS");
			solver.engine(ohh1Problem, SearchStrategy.DFS);
		}
		
		if(searchStrategy.equalsIgnoreCase(SearchStrategy.ASTAR.toString())){
			System.out.println("Starting engine with search strategy: " + "A*");
			solver.engine(ohh1Problem, SearchStrategy.ASTAR);
		}
		
		if(searchStrategy.equalsIgnoreCase(SearchStrategy.GREEDY.toString())){
			System.out.println("Starting engine with search strategy: " + "Greedy");
			solver.engine(ohh1Problem, SearchStrategy.GREEDY);
		}	
		
		
	}

}
