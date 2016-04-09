package ohh1.solver;

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
			return;
		}
		
		String heuristic = args[0];
		String searchStrategy = args[1];
		
		
		
	}

}
