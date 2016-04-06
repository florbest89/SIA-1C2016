package ohn1.gps.api;

import java.util.ArrayList;
import java.util.List;

import gps.api.GPSState;
import gps.common.BoardSelector;
import gps.common.Cell;

public class Ohn1State implements GPSState{
	
	private Cell[][] board;
	private List<RowStats> rowStats;
	private int board_size;
	
	public Ohn1State(int size){
		initializeBoard(size);
		initializeRowStats(size);
		this.board_size = size;
	}
	
	public Ohn1State(Cell[][] board, List<RowStats> stats, int size){
		this.board = board;
		this.rowStats = stats;
		this.board_size = size;
	}
	
	public boolean equals(Object state){
		
		if(state == null){
			return false;
		}
		
		if(state.getClass() != Ohn1State.class){
			return false;
		}
		
		Ohn1State other = (Ohn1State) state;
		
		if(other.getSize() != board_size){
			return false;
		}
		
		for(int i = 0; i < board_size ; i++){
			for(int j = 0; j < board_size ; j++){
				
				if(!other.getCell(i, j).equals(board[i][j])){
					return false;
				}
			}
		}
		
		return true;
		
	}
	
	public RowStats getRowStat(int row){
		return rowStats.get(row);
	}
	
	public Cell getCell(int i, int j){
		return board[i][j];
	}
	
	public void setCell(Cell cell,int i, int j){
		board[i][j] = cell;
	}
	
	public int getSize(){
		return board_size;
	}
	
	public Ohn1State clone(){
		return new Ohn1State(cloneBoard(), cloneStats(), board_size);
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
	
	private Cell[][] cloneBoard(){
		
		Cell[][] board = new Cell[board_size][board_size];
		
		for(int i = 0; i < board_size ; i++){
			for(int j = 0 ; j <= board_size ; j++){
				board[i][j] = this.board[i][j].clone();
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
