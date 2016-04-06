package gps.common;

public class BoardSelector {
	
	public static Cell[][] Selector(int size, int option){
		
		switch(size){
			case 4: return option == 1 ? size4board1() : size4board2();
			case 6: return option == 1 ? size6board1() : size6board2();
			default: return null;
		}  
	}
	
	private static Cell[][] size4board1(){
		
		Cell[][] board = new Cell[4][4];
		
		/*Row 0*/
		board[0][0] = new Cell(Color.Grey,false);
		board[0][1] = new Cell(Color.Grey,false);
		board[0][2] = new Cell(Color.Red,true);
		board[0][3] = new Cell(Color.Grey,false);
		
		/*Row 1*/
		board[1][0] = new Cell(Color.Grey,false);
		board[1][1] = new Cell(Color.Grey,false);
		board[1][2] = new Cell(Color.Grey,false);
		board[1][3] = new Cell(Color.Yellow,true);
		
		/*Row 2*/
		board[2][0] = new Cell(Color.Yellow,true);
		board[2][1] = new Cell(Color.Grey,false);
		board[2][2] = new Cell(Color.Grey,false);
		board[2][3] = new Cell(Color.Grey,false);
		
		/*Row 3*/
		board[3][0] = new Cell(Color.Red,true);
		board[3][1] = new Cell(Color.Red,true);
		board[3][2] = new Cell(Color.Grey,false);
		board[3][3] = new Cell(Color.Grey,false);
		
		return board;
	}
	
	private static Cell[][] size4board2(){
		
		Cell[][] board = new Cell[4][4];
		
		/*Row 0*/
		board[0][0] = new Cell(Color.Grey,false);
		board[0][1] = new Cell(Color.Grey,false);
		board[0][2] = new Cell(Color.Yellow,true);
		board[0][3] = new Cell(Color.Yellow,true);
		
		/*Row 1*/
		board[1][0] = new Cell(Color.Grey,false);
		board[1][1] = new Cell(Color.Grey,false);
		board[1][2] = new Cell(Color.Yellow,true);
		board[1][3] = new Cell(Color.Grey,false);
		
		/*Row 2*/
		board[2][0] = new Cell(Color.Grey,false);
		board[2][1] = new Cell(Color.Grey,false);
		board[2][2] = new Cell(Color.Grey,false);
		board[2][3] = new Cell(Color.Grey,false);
		
		/*Row 3*/
		board[3][0] = new Cell(Color.Grey,false);
		board[3][1] = new Cell(Color.Red,true);
		board[3][2] = new Cell(Color.Grey,false);
		board[3][3] = new Cell(Color.Grey,false);
		
		return board;
	}

	private static Cell[][] size6board1(){
		Cell[][] board = new Cell[6][6];
		
		/*Row 0*/
		board[0][0] = new Cell(Color.Grey,false);
		board[0][1] = new Cell(Color.Grey,false);
		board[0][2] = new Cell(Color.Grey,false);
		board[0][3] = new Cell(Color.Red,true);
		board[0][4] = new Cell(Color.Red,true);
		board[0][5] = new Cell(Color.Grey,false);
		
		/*Row 1*/
		board[1][0] = new Cell(Color.Grey,false);
		board[1][1] = new Cell(Color.Red,true);
		board[1][2] = new Cell(Color.Grey,false);
		board[1][3] = new Cell(Color.Grey,false);
		board[1][4] = new Cell(Color.Red,true);
		board[1][5] = new Cell(Color.Red,true);
		
		/*Row 2*/
		board[2][0] = new Cell(Color.Grey,false);
		board[2][1] = new Cell(Color.Grey,false);
		board[2][2] = new Cell(Color.Grey,false);
		board[2][3] = new Cell(Color.Grey,false);
		board[2][4] = new Cell(Color.Grey,false);
		board[2][5] = new Cell(Color.Grey,false);
		
		/*Row 3*/
		board[3][0] = new Cell(Color.Grey,false);
		board[3][1] = new Cell(Color.Yellow,true);
		board[3][2] = new Cell(Color.Grey,false);
		board[3][3] = new Cell(Color.Red,true);
		board[3][4] = new Cell(Color.Grey,false);
		board[3][5] = new Cell(Color.Grey,false);
		
		/*Row 4*/
		board[4][0] = new Cell(Color.Yellow,true);
		board[4][1] = new Cell(Color.Grey,false);
		board[4][2] = new Cell(Color.Grey,false);
		board[4][3] = new Cell(Color.Grey,false);
		board[4][4] = new Cell(Color.Grey,false);
		board[4][5] = new Cell(Color.Red,true);
		
		/*Row 5*/
		board[5][0] = new Cell(Color.Grey,false);
		board[5][1] = new Cell(Color.Grey,false);
		board[5][2] = new Cell(Color.Grey,false);
		board[5][3] = new Cell(Color.Grey,false);
		board[5][4] = new Cell(Color.Grey,false);
		board[5][5] = new Cell(Color.Red,true);
		
		return board;
	}

	private static Cell[][] size6board2(){
		Cell[][] board = new Cell[6][6];
		
		/*Row 0*/
		board[0][0] = new Cell(Color.Grey,false);
		board[0][1] = new Cell(Color.Grey,false);
		board[0][2] = new Cell(Color.Grey,false);
		board[0][3] = new Cell(Color.Grey,false);
		board[0][4] = new Cell(Color.Grey,false);
		board[0][5] = new Cell(Color.Grey,false);
		
		/*Row 1*/
		board[1][0] = new Cell(Color.Grey,false);
		board[1][1] = new Cell(Color.Grey,false);
		board[1][2] = new Cell(Color.Grey,false);
		board[1][3] = new Cell(Color.Grey,false);
		board[1][4] = new Cell(Color.Yellow,true);
		board[1][5] = new Cell(Color.Grey,false);
		
		/*Row 2*/
		board[2][0] = new Cell(Color.Grey,false);
		board[2][1] = new Cell(Color.Grey,false);
		board[2][2] = new Cell(Color.Yellow,true);
		board[2][3] = new Cell(Color.Grey,false);
		board[2][4] = new Cell(Color.Grey,false);
		board[2][5] = new Cell(Color.Red,false);
		
		/*Row 3*/
		board[3][0] = new Cell(Color.Grey,false);
		board[3][1] = new Cell(Color.Grey,false);
		board[3][2] = new Cell(Color.Grey,false);
		board[3][3] = new Cell(Color.Grey,false);
		board[3][4] = new Cell(Color.Yellow,true);
		board[3][5] = new Cell(Color.Grey,false);
		
		/*Row 4*/
		board[4][0] = new Cell(Color.Yellow,true);
		board[4][1] = new Cell(Color.Red,true);
		board[4][2] = new Cell(Color.Grey,false);
		board[4][3] = new Cell(Color.Grey,false);
		board[4][4] = new Cell(Color.Grey,false);
		board[4][5] = new Cell(Color.Grey,false);
		
		/*Row 5*/
		board[5][0] = new Cell(Color.Yellow,true);
		board[5][1] = new Cell(Color.Yellow,true);
		board[5][2] = new Cell(Color.Grey,false);
		board[5][3] = new Cell(Color.Red,true);
		board[5][4] = new Cell(Color.Grey,false);
		board[5][5] = new Cell(Color.Grey,false);
		
		return board;
	}

}
