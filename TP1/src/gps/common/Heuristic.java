package gps.common;

import java.util.HashMap;

import ohh1.gps.api.Ohh1State;

public enum Heuristic {
	SwapsPerRow, ColumnColorFix;

	public static Integer ColorPerColHValue(Ohh1State state){
		Integer hValue = 0;
		int missingColors = 0;
		int invalidRows = 0;
		int colClusterCorrection = 0;
		HashMap<Integer, Boolean> RowStates = new HashMap<Integer, Boolean>();
		
		for (int i = 0; i < state.BOARD_SIZE; i++)
		{
			boolean isValid = isRowValid(state.getBoard(), state.BOARD_SIZE, i);
			RowStates.put(i, isValid);
			
			if (!isValid){
				invalidRows++;
			}
		}
		
		//Check column states
		for (int i = 0; i < state.BOARD_SIZE; i++)
		{
			ColumnState colState = getMinSwapsInCol(state.getBoard(), state.BOARD_SIZE, i, RowStates);
			
			missingColors += colState.countYellow - colState.countRed; 
			colClusterCorrection += colState.swaps;				
		}
		
		hValue = missingColors + colClusterCorrection + invalidRows;
		
		if (hValue == 0)
		{
			//Add swaps needed to fix group duplicates
			int duplicateRows = getDuplicateRows(state.getBoard(), state.BOARD_SIZE);
			int duplicateCols = getDuplicateCols(state.getBoard(), state.BOARD_SIZE);

			hValue += (duplicateRows + duplicateCols) / 2;
		}
						
		return hValue;
	}
				
	/**
	 * Returns TRUE if the row is valid
	 * @param board
	 * @param size
	 * @param row
	 * @return
	 */
	private static boolean isRowValid(int[][] board, int size, int row)
	{
		int streakColor = board[row][0];
		int colorCount = 1;
		
		for (int i = 1; i < size; i++)
		{
			if (Cell.sameColor(board[row][i], streakColor)){
				colorCount++;
			}
			else
			{
				colorCount = 1;
				streakColor = board[row][i];	
			}
			
			if (colorCount >= 3){
				return false;
			}				
		}
		
		return true;
	}	
	
	public static Integer getSwapsPerRowHValue(Ohh1State state)
	{
		HashMap<Integer, Boolean> RowStates = new HashMap<Integer, Boolean>();
		int minSwapsCols = 0;
		int unbalancedColorColSwap = 0;
		Integer hValue = 0;

		//Check for minimum number of swaps within a row
		for (int i = 0; i < state.BOARD_SIZE; i++)
		{
			int minSwapsRows = getMinSwapsInRow(state.getBoard(), state.BOARD_SIZE, i);
			
			if (minSwapsRows == 0)
			{
				RowStates.put(i, true);
			} else {
				RowStates.put(i, false);
			}
			
			hValue += minSwapsRows;
		}
		
		//Check column states
		for (int i = 0; i < state.BOARD_SIZE; i++)
		{
			ColumnState colState = getMinSwapsInCol(state.getBoard(), state.BOARD_SIZE, i, RowStates);
				
			minSwapsCols += colState.swaps;
						
			if (colState.countRed != colState.countYellow)
			{
				unbalancedColorColSwap++;
			}			
		}
		
		//Add swaps needed to fix group of colors
		hValue += (minSwapsCols / 2);
		
		if (hValue == 0)
		{
			if (unbalancedColorColSwap == 0)
			{
				//Add swaps needed to fix group duplicates
				int duplicateRows = getDuplicateRows(state.getBoard(), state.BOARD_SIZE);
				int duplicateCols = getDuplicateCols(state.getBoard(), state.BOARD_SIZE);

				hValue += (duplicateRows + duplicateCols) / 2;
			} else {
				//Add swaps to fix color balance in columns
				hValue += (unbalancedColorColSwap / 2);
			}
		}
				
		return hValue;
	}
	
	/**
	 * Calculates amunt of duplicates pairs of columns	
	 * @param board
	 * @param size
	 * @return
	 */
	private static int getDuplicateCols(int[][] board, int size){
		int duplicates = 0;
		boolean flag;
		for (int i = 0; i < size; i++){
			for (int j = i + 1; j < size; j++){
				flag = true;
				for (int k = 0; k < size && flag; k++) {
					if (!Cell.sameColor(board[k][i], board[k][j])){
						flag = false;
					} 					
				}
				if (flag)
				{
					duplicates++;
				}
			}
		}
		return duplicates;
	}
	
	/**
	 * Calculates amunt of duplicates pairs of rows	
	 * @param board
	 * @param size
	 * @return
	 */
	private static int getDuplicateRows(int[][] board, int size){
		int duplicates = 0;
		boolean flag;
		for (int i = 0; i < size; i++){
			for (int j = i + 1; j < size; j++){
				flag = true;
				for (int k = 0; k < size && flag; k++) {
					if (!Cell.sameColor(board[i][k], board[j][k])){
						flag = false;
					} 					
				}
				if (flag)
				{
					duplicates++;
				}
			}
		}
		
		return duplicates;
	}
	
	/**
	 * Returns column state. Includes swaps needed to fix clusters and number of RED and YELLOW tiles	
	 * @param board
	 * @param size
	 * @param col
	 * @param RowStates
	 * @return
	 */
	private static ColumnState getMinSwapsInCol(int[][] board, int size, int col, HashMap<Integer, Boolean> RowStates)
	{
		
		boolean streakRowsComplete = RowStates.get(0);
		int swaps = 0;
		int colorCount = 1;
		int countRed = 0;
		int countYellow = 0;
		int streakColor = board[0][col];
		
		if (Cell.isRed(board[0][col]))
		{
			countRed++;
		}else{
			countYellow++;
		}
				
		for (int i = 1; i < size; i++)
		{
			if (Cell.sameColor(board[i][col], streakColor)){
				colorCount++;
				streakRowsComplete = streakRowsComplete && RowStates.get(i);
			}
			else
			{
				if (colorCount >= 3 && streakRowsComplete)
				{
					swaps++;
				}
				
				colorCount = 1;
				streakColor = board[i][col];
				streakRowsComplete = RowStates.get(i);
			}
			
			if (Cell.isRed(board[i][col]))
			{
				countRed++;
			}else{
				countYellow++;
			}
		}
		
		if (colorCount >= 3 && streakRowsComplete)
		{
			swaps++;
		}
		
		ColumnState colState = new ColumnState(swaps, countRed, countYellow);
		
		return colState; 
	}
	
	/**
	 * Calculates minimum number of swaps within a row to fix clusters 
	 * @param board
	 * @param size
	 * @param row
	 * @return
	 */
	private static int getMinSwapsInRow(int[][] board, int size, int row)
	{
		int maxCount = 1;
		int streakColor = board[row][0];
		int colorCount = 1;
		
		for (int i = 1; i < size; i++)
		{
			if (Cell.sameColor(board[row][i], streakColor)){
				colorCount++;
			}
			else
			{
				colorCount = 1;
				streakColor = board[row][i];	
			}
					
			maxCount = Integer.max(colorCount, maxCount);
		}
		
		return maxCount / 3; 
	}	
}



