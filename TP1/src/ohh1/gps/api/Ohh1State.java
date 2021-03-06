package ohh1.gps.api;

import java.util.ArrayList;
import java.util.List;

import gps.api.GPSState;
import gps.common.*;


public class Ohh1State implements GPSState{
	
	private int[][] board;
	private List<RowStats> rowStats;
	public static int BOARD_SIZE = 6;
	private List<String> appliedRule= new ArrayList<String>();
	
	public Ohh1State(){
		initializeBoard(BOARD_SIZE);
		initializeRowStats(BOARD_SIZE);
	}
	
	public Ohh1State(int[][] board, List<RowStats> stats, List<String> rules){
		this.board = board;
		this.rowStats = stats;
		this.appliedRule = rules;
	}
	
	public int[][] getBoard(){
		return board;
	}
	
	@Override
	public int hashCode() {
		int hash = 0;
		int i = 0;
		for (int[] row : this.board) {
			for (int slot : row) {
				if (slot != -1) {
					hash += Math.pow(10, i) * slot;
				}
				i++;
			}
		}
		return hash;
	}
	
	@Override
	public boolean equals(Object state){
		
		if(state == null){
			return false;
		}
		
		if(state.getClass() != Ohh1State.class){
			return false;
		}
		
		Ohh1State other = (Ohh1State) state;
		
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
		Ohh1State.BOARD_SIZE = size;
	}
	
	public RowStats getRowStat(int row){
		return rowStats.get(row);
	}
	
	public void CompleteRow(int row){
		rowStats.get(row).Complete();
	}
	
	public void BreakRow(int row){
		rowStats.get(row).Break();
	}
	
	public int getCell(int i, int j){
		return board[i][j];
	}
	
	public void setCell(int cell,int i, int j){
		board[i][j] = cell;
	}
	
	public Ohh1State clone(){
		return new Ohh1State(cloneBoard(), cloneStats(), cloneAppliedRule());
	}
	
	private void initializeBoard(int size){
		this.board = BoardSelector.Selector(size);
	}
	
	private void initializeRowStats(int size){
		
		int i = 0;
		
		this.rowStats = new ArrayList<RowStats>();
		
		while(i < size){
			rowStats.add(new RowStats(i));
			i++;
		}
	}
	
	private int[][] cloneBoard(){
		
		int[][] board = new int[BOARD_SIZE][BOARD_SIZE];
		
		for(int i = 0; i < BOARD_SIZE ; i++){
			for(int j = 0 ; j < BOARD_SIZE ; j++){
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

	private List<String> cloneAppliedRule(){
		List<String> cloneAR = new ArrayList<String>();
		
		for(String each : appliedRule){
			cloneAR.add(each);
		}
		
		return cloneAR;
	}
	
	public List<String> getAppliedRule() {
		return appliedRule;
	}

	public void setAppliedRule(List<String> appliedRule) {
		this.appliedRule = appliedRule;
	}

	@Override
	public String toString(){
		String textBoard = "";
		
		textBoard = "===================\n";
		for(int i = 0; i < BOARD_SIZE ; i++){
			for(int j = 0 ; j < BOARD_SIZE ; j++){
				
				if(this.board[i][j] == Cell.Grey.getValue()){
					textBoard += "G ";
				}
				else if(this.board[i][j] == Cell.Red.getValue() || this.board[i][j] == Cell.RedFixed.getValue()){
					textBoard += "R ";
				}
				else {
					textBoard += "Y ";
				}
				
			}
			textBoard += "\n";
		}
		
		return textBoard;
	}
	

	public void addAppliedRule(String rule) {
		this.appliedRule.add(rule);
	}
}
