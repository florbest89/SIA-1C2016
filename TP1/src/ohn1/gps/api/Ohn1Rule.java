package ohn1.gps.api;

import gps.api.GPSRule;
import gps.api.GPSState;
import gps.common.Cell;
import gps.exception.NotAppliableException;

public class Ohn1Rule implements GPSRule{	
	
	private int row;
	private int col1,col2;
	
	@Override
	public Integer getCost() {
		/*Each rule allows for one swap to take place*/
		return 1;
	}

	@Override
	public String getName() {
		return "Se realiza un swap en la fila " + row + " entre las columnas " + col1 + " y " + col2;
	}

	@Override
	public GPSState evalRule(GPSState state) throws NotAppliableException {
		
		Ohn1State clone = ((Ohn1State) state).clone();
		
		if(clone.getRowStat(row).isComplete()){
			throw new NotAppliableException();
		}
		
		Cell cell1 = clone.getCell(row, col1);
		Cell cell2 = clone.getCell(row, col2);
		
		if(cell1.isFixed() || cell2.isFixed()){
			throw new NotAppliableException();
		}
		
		if(cell1.getColor().equals(cell2.getColor())){
			throw new NotAppliableException();
		}
		
		/*Swap cells*/
		clone.setCell(cell1, row, col2);
		clone.setCell(cell2, row, col1);
		
		/*Check if swapping didn't generate an invalid state*/
		if(!(isValid(col1,clone) && isValid(col2,clone))){
			throw new NotAppliableException();
		}
		
		return clone;
	}
	
	private boolean isValid(int col, Ohn1State state){
		
		Cell cell = state.getCell(row, col);
		
		int count = 1;
		boolean breakFlag = false;
		
		/*Check to the left*/
		for(int j = col - 1 ; j >= 0 && j != col - 3 && !breakFlag ; j--){
			if(state.getCell(row, j).getColor().equals(cell.getColor())){
				count ++;
			} else {
				breakFlag = true;
			}
		}
		
		breakFlag = false;
		
		/*Check to the right*/
		for(int j = col + 1 ; j < state.getSize() && j != col + 3 && !breakFlag ; j++){
			if(state.getCell(row, j).getColor().equals(cell.getColor())){
				count ++;
			} else {
				breakFlag = true;
			}
		}
		
		if(count >= 3){
			return false;
		}
		
		return true;
	}

}
