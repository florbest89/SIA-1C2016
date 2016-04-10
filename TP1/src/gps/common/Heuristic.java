package gps.common;

import ohh1.gps.api.Ohh1State;

public enum Heuristic {
	SwapsPerRow, ColorPerCol;

	public static Integer getSwapsPerRowValue(Ohh1State state)
	{
		int[][] board = state.getBoard();
		return null;
	}
	
	private int getMaxSwapsInRow(int[][] board, int row)
	{
		
		return 0;
	}

}