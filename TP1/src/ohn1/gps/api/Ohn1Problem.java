package ohn1.gps.api;

import java.util.List;

import gps.api.GPSProblem;
import gps.api.GPSRule;
import gps.api.GPSState;

import gps.common.*;

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
		
		//TODO: CheckSameRows
		
		
		return false;
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

	@Override
	public List<GPSRule> getRules() {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public Integer getHValue(GPSState state) {
		// TODO Auto-generated method stub
		return null;
	}

}
