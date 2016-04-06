package gps.common;

public class Cell {
	
	private Color color;
	private boolean fixed;
	
	public Cell(Color color, boolean fixed){
		this.color = color;
		this.fixed = fixed;
	}
	
	public void setColor(Color color){
		this.color = color;
	}
	
	public Color getColor(){
		return this.color;
	}
	
	public boolean isFixed(){
		return fixed;
	}
	
	public Cell clone(){
		return new Cell(color,fixed);
	}
	
	@Override
	public boolean equals(Object other){
		
		if(other == null){
			return false;
		}
		
		if(other.getClass() != Cell.class){
			return false;
		}
		
		Cell other_cell = (Cell) other;
		
		return fixed == other_cell.isFixed() && color.equals(other_cell.getColor());
		
	}
	
}
