package gps.common;

public enum Cell {
	Red(0),	Yellow(1), Grey(2), RedFixed(3), YellowFixed(4);
	
	private final int value;
	
	private Cell(int value){
		this.value = value;
	}
	
	public int getValue(){
		return value;
	}
	
	public static boolean isFixed(int value){
		return value == Red.getValue() || value == Yellow.getValue();
	}
	
	public static boolean sameColor(int color1, int color2){
		
		if(color1 == Red.getValue() || color1 == RedFixed.getValue()){
			return color2 == Red.getValue() || color2 == RedFixed.getValue();
		}
		
		if(color1 == Yellow.getValue() || color1 == Yellow.getValue()){
			return color2 == Yellow.getValue() || color2 == YellowFixed.getValue();
		}
		
		return color1 == color2;
	}
}
