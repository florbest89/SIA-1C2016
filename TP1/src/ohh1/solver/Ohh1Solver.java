package ohh1.solver;

import gps.GPSEngine;
import gps.SearchStrategy;
import gps.api.GPSProblem;
import gps.common.BoardSelector;
import gps.common.Heuristic;
import ohh1.gps.api.Ohh1Engine;
import ohh1.gps.api.Ohh1Problem;
import ohh1.gps.api.Ohh1State;

public class Ohh1Solver {

	public static void main(String[] args) {

		/*
		 * Arguments 1. Heuristic 2. Search strategy 3. Board size 4. Board
		 * option
		 * 
		 */

		if (args.length == 4) {
			try {
				int boardSize = Integer.parseInt(args[2]);

				if (boardSize == 4 || boardSize == 6) {
					Ohh1State.setSize(boardSize);
					System.out.println("Game board size: " + boardSize + "x" + boardSize);
				} else {
					System.out.println("Invalid size! Size must be '4' or '6'");
					return;
				}

			} catch (NumberFormatException ex) {
				System.out.println("Invalid arguments! Size must be a number");
				return;
			}

			try {
				int boption = Integer.parseInt(args[3]);

				if(Integer.parseInt(args[2]) == 6){
					if (boption == 1 || boption == 2 || boption == 3 || boption == 4 || boption == 5) {
						BoardSelector.OPTION = boption;
						System.out.println("Board option: " + boption);
					} else {
						System.out.println("Invalid option! Must be 1, 2, 3, 4 or 5");
						return;
					}
				}else if (Integer.parseInt(args[2]) == 2){					
					if (boption == 1 || boption == 2) {
						BoardSelector.OPTION = boption;
						System.out.println("Board option: " + boption);
					} else {
						System.out.println("Invalid option! Must be 1 or 2");
						return;
					}
					
				}

			} catch (NumberFormatException ex) {
				System.out.println("Invalid arguments! Board option must be a number");
				return;
			}

		} else {
			System.out.println("Invalid arguments!");
			System.out.println("Arguments must be (in order) : Heuristic, Search strategy, Board size, Board option");
			System.out.println("Heuristics available: SwapsPerRows, ColumnColorFix");
			System.out.println("Search strategies available: IDDFS, BFS, DFS, ASTAR, GREEDY");
			System.out.println("Boards of size 4 or 6");
			System.out.println("Board option is 1 or 2");
			return;
		}

		String heuristic = args[0];

		GPSProblem ohh1Problem = new Ohh1Problem();

		if (heuristic.equalsIgnoreCase("swapsperrow")) {
			Ohh1Problem.setH(Heuristic.SwapsPerRow);
		} else if (heuristic.equalsIgnoreCase("columncolorfix")) {
			Ohh1Problem.setH(Heuristic.ColumnColorFix);
		} else {
			System.out.println("Invalid arguments! Heuristics must be 'SwapsPerRow' or 'ColumnColorFix'");
			return;
		}

		GPSEngine solver = new Ohh1Engine();

		String searchStrategy = args[1];

		if (searchStrategy.equalsIgnoreCase(SearchStrategy.IDDFS.toString())) {
			System.out.println("Starting engine with search strategy: " + "Iterative");
			solver.engine(ohh1Problem, SearchStrategy.IDDFS);
		}

		if (searchStrategy.equalsIgnoreCase(SearchStrategy.BFS.toString())) {
			System.out.println("Starting engine with search strategy: " + "BFS");
			solver.engine(ohh1Problem, SearchStrategy.BFS);
		}

		if (searchStrategy.equalsIgnoreCase(SearchStrategy.DFS.toString())) {
			System.out.println("Starting engine with search strategy: " + "DFS");
			solver.engine(ohh1Problem, SearchStrategy.DFS);
		}

		if (searchStrategy.equalsIgnoreCase(SearchStrategy.ASTAR.toString())) {
			System.out.println("Starting engine with search strategy: " + "A*");
			solver.engine(ohh1Problem, SearchStrategy.ASTAR);
		}

		if (searchStrategy.equalsIgnoreCase(SearchStrategy.GREEDY.toString())) {
			System.out.println("Starting engine with search strategy: " + "Greedy");
			solver.engine(ohh1Problem, SearchStrategy.GREEDY);
		}

	}

}
