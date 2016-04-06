package ohn1.gps.api;

public class RowStats {
	
	private int row;
	private boolean complete;
	
	public RowStats(int row){
		this.row = row;
		complete = false;
	}
	
	public RowStats(int row, boolean complete){
		this.row = row;
		this.complete = complete;
	}
	
	public void Complete(){
		complete = true;
	}
	
	public boolean isComplete(){
		return complete;
	}

	public int getRow() {
		return row;
	}
	
	public RowStats clone(){
		return new RowStats(row,complete);
	}
	
}
