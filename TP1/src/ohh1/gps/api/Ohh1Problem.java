package ohh1.gps.api;

import java.util.ArrayList;
import java.util.List;

import gps.api.GPSProblem;
import gps.api.GPSRule;
import gps.api.GPSState;
import gps.common.Cell;

public class Ohh1Problem implements GPSProblem{
	//TODO: BORRAR
	static Ohh1State board;
	
	@Override
	public GPSState getInitState() {
		
		//TODO: EMPROLIJAR METODO.
		/*
		 * return prepareBoard(new Ohh1State());
		 */
		
		this.board = new Ohh1State();
		System.out.println(this.board.toString());
		prepareBoard(this.board);
		System.out.println(this.board.toString());
		return this.board;
	}
	@Override
	public boolean isGoal(GPSState state) {
		
		Ohh1State ohh1State = (Ohh1State) state;
		
		/*
		 * Check if the rows are complete
		 * If they aren't it means that at least one breaks the rule of three cells of same color together
		 * 
		 */
		 
		for(int i = 0 ; i < Ohh1State.BOARD_SIZE ; i++){
			if(!ohh1State.getRowStat(i).isComplete()){
				return false;
			}
		}
		
		/*Check that there are no three or more cells adjacent of same color in a column*/
		if(!checkThreeCellsRuleInCol(ohh1State)){
			return false;
		}
		
		if(checkSameCols(ohh1State)){
			return false;
		}
		
		if(checkSameRows(ohh1State)){
			return false;
		}
		
		if(!validColorBalanceInCols(ohh1State)){
			return false;
		}
				
		return true;
	}
	
	public void prepareBoard(Ohh1State state){		
		
		for(int i = 0; i < Ohh1State.BOARD_SIZE ; i++){
			
			int red = Ohh1State.BOARD_SIZE / 2;
			int yellow = Ohh1State.BOARD_SIZE / 2;
			
			/*Check how many red and yellow cells needed*/
			for(int j = 0; j < Ohh1State.BOARD_SIZE ; j++){
				
				if(state.getCell(i, j) == Cell.RedFixed.getValue()){
					red --;
				}
				
				if(state.getCell(i, j) == Cell.YellowFixed.getValue()){
					yellow--;
				}				
			}			
			
			/*Complete row*/
			for(int j = 0 ; j < Ohh1State.BOARD_SIZE && (yellow > 0 || red > 0) ; j++){
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
			
			/*Check for complete rows*/
			for(int row = 0 ; row < Ohh1State.BOARD_SIZE ; row++){
				
				boolean notcomplete = false;
				int current = Cell.Grey.getValue();
				int sameColor = 1;
				
				for(int col = 0 ; col < Ohh1State.BOARD_SIZE && !notcomplete ; col++){
				
					int cell = state.getCell(row, col);
						
					if(!Cell.sameColor(current, cell)){
						current = cell;
						sameColor = 1;
					} else {
						sameColor++;
						if(sameColor >= 3){
							notcomplete = true;
						}
					}
				}
				
				if(!notcomplete){
					state.CompleteRow(row);					
				}
			}
			
		}
		
	}
	
	private boolean checkThreeCellsRuleInCol(Ohh1State state){
		
		for(int col = 0 ; col < Ohh1State.BOARD_SIZE; col++){
			int sameColor = 1;
			int current = Cell.Grey.getValue();
			
			for(int row = 0 ; row < Ohh1State.BOARD_SIZE; row++){
				
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
		}
		
		return true;		
	}

	private boolean checkSameCols(Ohh1State state){
		
		boolean check = false;
		
		for(int j = 0 ; j < Ohh1State.BOARD_SIZE && !check; j++){
			for(int k = j + 1 ; k < Ohh1State.BOARD_SIZE && !check; k++){
				
				check = true;
				
				for(int i = 0; i < Ohh1State.BOARD_SIZE && check; i++){
					check = check && Cell.sameColor(state.getCell(i, j), state.getCell(i, k));
				}
				
				if(check){
					return true;
				}
			}
		}
		
		return false;
		
	}
	
	private boolean checkSameRows(Ohh1State state){
		boolean check = false;
		
		for(int i = 0 ; i < Ohh1State.BOARD_SIZE && !check; i++){
			for(int k = i + 1 ; k < Ohh1State.BOARD_SIZE && !check; k++){
				
				check = true;
				
				for(int j = 0 ; j < Ohh1State.BOARD_SIZE && check; j++){
					check = check && Cell.sameColor(state.getCell(i, j), state.getCell(k, j));
				}
				
				if(check){
					return true;
				}
			}
		}
		
		return false;
	}

	private boolean validColorBalanceInCols(Ohh1State state){		
		
		for(int j = 0 ; j < Ohh1State.BOARD_SIZE ; j++){
			
			int red = Ohh1State.BOARD_SIZE / 2;
			int yellow = Ohh1State.BOARD_SIZE / 2;
			
			for(int i = 0; i < Ohh1State.BOARD_SIZE; i++){
				
				int cell = state.getCell(i, j);
				
				if(Cell.sameColor(cell, Cell.Red.getValue())){
					red--;
				} else {
					yellow--;
				}
			}
			
			if(red != yellow){
				return false;
			}
		}
		
		return true;
		
	}
	
	@Override
	public List<GPSRule> getRules() {
		
		List<GPSRule> rules = new ArrayList<GPSRule>();
		
		for(int i = 0; i < Ohh1State.BOARD_SIZE ; i++){
			for(int j = 0; j < Ohh1State.BOARD_SIZE ; j++){
				for(int k = j + 1; k < Ohh1State.BOARD_SIZE ; k++){
					rules.add((GPSRule) new Ohh1Rule(i,j,k));
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
