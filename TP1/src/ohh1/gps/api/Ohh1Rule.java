package ohh1.gps.api;

import gps.api.GPSRule;
import gps.api.GPSState;
import gps.common.*;
import gps.exception.NotAppliableException;

public class Ohh1Rule implements GPSRule{	
	
	private int row;
	private int col1,col2;
	
	public Ohh1Rule(int row, int col1, int col2) {
		this.row = row;
		this.col1 = col1;
		this.col2 = col2;
	}
	
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
		
		int cell1 = ((Ohh1State) state).getCell(row, col1);
		int cell2 = ((Ohh1State) state).getCell(row, col2);
		String ruleToApply = String.valueOf(row)+String.valueOf(col1)+String.valueOf(cell1)+String.valueOf(col2)+String.valueOf(cell2);
		String ruleToApplyInverse = String.valueOf(row)+String.valueOf(col1)+String.valueOf(cell2)+String.valueOf(col2)+String.valueOf(cell1);

		
		if(((Ohh1State) state).getAppliedRule().contains(ruleToApply))
			throw new NotAppliableException();
			
		Ohh1State clone = ((Ohh1State) state).clone();
		
		if(Cell.isFixed(cell1) || Cell.isFixed(cell2)){
			throw new NotAppliableException();
		}
		
		if(Cell.sameColor(cell1, cell2)){
			throw new NotAppliableException();
		}
		
		/*Swap cells*/
		clone.setCell(cell1, row, col2);
		clone.setCell(cell2, row, col1);
		
		/*Check if swapping didn't generate an invalid state*/
		if(!(isValid(col1,clone) && isValid(col2,clone))){
			throw new NotAppliableException();
		}
		
		if(isRowComplete(clone)){
			clone.CompleteRow(row);
		}
		
		clone.addAppliedRule(ruleToApply);
		clone.addAppliedRule(ruleToApplyInverse);
		return clone;
	}
	
	private boolean isValid(int col, Ohh1State state){
		
		int cell = state.getCell(row, col);
		
		int count = 1;
		boolean breakFlag = false;
		
		/*Check to the left*/
		for(int j = col - 1 ; j >= 0 && j != col - 3 && !breakFlag ; j--){
			if(Cell.sameColor(state.getCell(row, j), cell)){
				count ++;
			} else {
				breakFlag = true;
			}
		}
		
		breakFlag = false;
		
		/*Check to the right*/
		for(int j = col + 1 ; j < Ohh1State.BOARD_SIZE && j != col + 3 && !breakFlag ; j++){
			if(Cell.sameColor(state.getCell(row, j), cell)){
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
	
	private boolean isRowComplete(Ohh1State state){
		
		int current = Cell.Grey.getValue();
		int sameColor = 1;
		
		for(int col = 0 ; col < Ohh1State.BOARD_SIZE; col++){
		
			int cell = state.getCell(row, col);
				
			if(!Cell.sameColor(current, cell)){
				current = cell;
				sameColor = 1;
			} else {
				sameColor++;
				if(sameColor >= 3){
					return false;
				}
			}
		}
		
		return true;
	}

}
