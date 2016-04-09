package ohn1.gps.api;

import java.util.ArrayList;
import java.util.List;

import gps.api.GPSProblem;
import gps.api.GPSRule;
import gps.api.GPSState;
import gps.common.Cell;

public class Ohn1Problem implements GPSProblem{

	@Override
	public GPSState getInitState() {
		return new Ohn1State();
	}

	@Override
	public boolean isGoal(GPSState state) {
		
		Ohn1State ohn1State = (Ohn1State) state;
		
		/*
		 * Check if the rows are complete
		 * If they aren't it means that at least one breaks the rule of three cells of same color together
		 * 
		 */
		 
		for(int i = 0 ; i < Ohn1State.BOARD_SIZE ; i++){
			if(!ohn1State.getRowStat(i).isComplete()){
				return false;
			}
		}
		
		/*Check that there are no three or more cells adjacent of same color in a column*/
		if(!checkThreeCellsRuleInCol(ohn1State)){
			return false;
		}
		
		if(checkSameCols(ohn1State)){
			return false;
		}
		
		if(checkSameRows(ohn1State)){
			return false;
		}
				
		return true;
	}
	
	public void prepareBoard(Ohn1State state){
		
		for(int i = 0; i < Ohn1State.BOARD_SIZE ; i++){
			
			int red = Ohn1State.BOARD_SIZE / 2;
			int yellow = Ohn1State.BOARD_SIZE / 2;
			
			for(int j = 0 ; j < Ohn1State.BOARD_SIZE && yellow > 0 && red > 0 ; j++){
				int cell = state.getCell(i, j);
				
				if(cell == Cell.Grey.getValue()){
					if(red > 0){
						state.setCell(Cell.Red.getValue(), i, j);
						red--;
					} else {
						state.setCell(Cell.Yellow.getValue(), i, j);
						yellow--;
					}
				}
			}
		}
		
	}
	
	private boolean checkThreeCellsRuleInCol(Ohn1State state){
		
		for(int col = 0 ; col < Ohn1State.BOARD_SIZE; col++){
			int sameColor = 0;
			int current = Cell.Grey.getValue();
			
			for(int row = 0 ; row < Ohn1State.BOARD_SIZE; row++){
				
				int cell = state.getCell(row, col);
				
				if(!Cell.sameColor(current, cell)){
					current = cell;
					sameColor = 0;
				} else {
					sameColor++;
					if(sameColor >= 3){
						return false;
					}
				}
			}
		}
		
		return true;		
	}

	private boolean checkSameCols(Ohn1State state){
		
		boolean check = false;
		
		for(int j = 0 ; j < Ohn1State.BOARD_SIZE && !check; j++){
			for(int k = j + 1 ; k < Ohn1State.BOARD_SIZE && !check; k++){
				
				check = true;
				
				for(int i = 0; i < Ohn1State.BOARD_SIZE && check; i++){
					check = check && Cell.sameColor(state.getCell(i, j), state.getCell(i, k));
				}
				
				if(check){
					return true;
				}
			}
		}
		
		return false;
		
	}
	
	private boolean checkSameRows(Ohn1State state){
		boolean check = false;
		
		for(int i = 0 ; i < Ohn1State.BOARD_SIZE && !check; i++){
			for(int k = i + 1 ; k < Ohn1State.BOARD_SIZE && !check; k++){
				
				check = true;
				
				for(int j = 0 ; j < Ohn1State.BOARD_SIZE && check; j++){
					check = check && Cell.sameColor(state.getCell(i, j), state.getCell(k, j));
				}
				
				if(check){
					return true;
				}
			}
		}
		
		return false;
	}

	@Override
	public List<GPSRule> getRules() {
		
		List<GPSRule> rules = new ArrayList<GPSRule>();
		
		for(int i = 0; i < Ohn1State.BOARD_SIZE ; i++){
			for(int j = 0; j < Ohn1State.BOARD_SIZE ; j++){
				for(int k = j + 1; k < Ohn1State.BOARD_SIZE ; k++){
					rules.add((GPSRule) new Ohn1Rule(i,j,k));
				}
			}
		}
		
		return rules;
	}

	@Override
	public Integer getHValue(GPSState state) {
		// TODO Auto-generated method stub
		return null;
	}

}
