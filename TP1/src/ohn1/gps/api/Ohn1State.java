package ohn1.gps.api;

import java.util.ArrayList;
import java.util.List;

import gps.api.GPSState;
import gps.common.*;


public class Ohn1State implements GPSState{
	
	private int[][] board;
	private List<RowStats> rowStats;
	public static int BOARD_SIZE = 6;
	
	public Ohn1State(){
		initializeBoard(BOARD_SIZE);
		initializeRowStats(BOARD_SIZE);
	}
	
	public Ohn1State(int[][] board, List<RowStats> stats){
		this.board = board;
		this.rowStats = stats;
	}
	
	public int[][] getBoard(){
		return board;
	}
	
	public boolean equals(Object state){
		
		if(state == null){
			return false;
		}
		
		if(state.getClass() != Ohn1State.class){
			return false;
		}
		
		Ohn1State other = (Ohn1State) state;
		
		for(int i = 0; i < BOARD_SIZE ; i++){
			for(int j = 0; j < BOARD_SIZE ; j++){
				
				if(other.getCell(i, j) != board[i][j]){
					return false;
				}
			}
		}
		
		return true;
		
	}
	
	/*It is only used when the solver starts*/
	public static void setSize(int size){
		Ohn1State.BOARD_SIZE = size;
	}
	
	public RowStats getRowStat(int row){
		return rowStats.get(row);
	}
	
	public void CompleteRow(int row){
		rowStats.get(row).Complete();
	}
	
	public int getCell(int i, int j){
		return board[i][j];
	}
	
	public void setCell(int cell,int i, int j){
		board[i][j] = cell;
	}
	
	public Ohn1State clone(){
		return new Ohn1State(cloneBoard(), cloneStats());
	}
	
	private void initializeBoard(int size){
		this.board = BoardSelector.Selector(size,1);
	}
	
	private void initializeRowStats(int size){
		
		int i = 0;
		
		this.rowStats = new ArrayList<RowStats>();
		
		while(i < size){
			rowStats.add(new RowStats(i));
		}
	}
	
	private int[][] cloneBoard(){
		
		int[][] board = new int[BOARD_SIZE][BOARD_SIZE];
		
		for(int i = 0; i < BOARD_SIZE ; i++){
			for(int j = 0 ; j <= BOARD_SIZE ; j++){
				board[i][j] = this.board[i][j];
			}
		}
		
		return board;
	}
	
	private List<RowStats> cloneStats(){
		List<RowStats> stats = new ArrayList<RowStats>();
		
		for(RowStats each : rowStats){
			stats.add(each.clone());
		}
		
		return stats;
	}
}
