package gps.common;

public class BoardSelector {
	
	public static int[][] Selector(int size){
		
		double num = Math.random();
		
		switch(size){
			case 4: return num > 0.5? size4board1() : size4board2();
			case 6: return num > 0.5 ? size6board1() : size6board2();
			case 8: return num > 0.5 ? size8board1() : size8board2(); 
			default: return null;
		}  
	}
	
	private static int[][] size4board1(){
		
		int[][] board = new int[4][4];
		
		/*Row 0*/
		board[0][0] = Cell.Grey.getValue();
		board[0][1] = Cell.Grey.getValue();		
		board[0][2] = Cell.RedFixed.getValue();		
		board[0][3] = Cell.RedFixed.getValue();
		
		/*Row 1*/
		board[1][0] = Cell.Grey.getValue();
		board[1][1] = Cell.Grey.getValue();
		board[1][2] = Cell.Grey.getValue();
		board[1][3] = Cell.YellowFixed.getValue();
		
		/*Row 2*/
		board[2][0] = Cell.YellowFixed.getValue();
		board[2][1] = Cell.Grey.getValue();
		board[2][2] = Cell.Grey.getValue();
		board[2][3] = Cell.Grey.getValue();
		
		/*Row 3*/
		board[3][0] = Cell.RedFixed.getValue();
		board[3][1] = Cell.RedFixed.getValue();
		board[3][2] = Cell.Grey.getValue();
		board[3][3] = Cell.Grey.getValue(); 
		
		return board;
	}
	
	private static int[][] size4board2(){
		
		int[][] board = new int[4][4];
		
		/*Row 0*/
		board[0][0] = Cell.Grey.getValue();
		board[0][1] = Cell.Grey.getValue();
		board[0][2] = Cell.YellowFixed.getValue();
		board[0][3] = Cell.YellowFixed.getValue();
		
		/*Row 1*/
		board[1][0] = Cell.Grey.getValue();
		board[1][1] = Cell.Grey.getValue();
		board[1][2] = Cell.YellowFixed.getValue();
		board[1][3] = Cell.Grey.getValue();
		
		/*Row 2*/
		board[2][0] = Cell.Grey.getValue();
		board[2][1] = Cell.Grey.getValue();
		board[2][2] = Cell.Grey.getValue();
		board[2][3] = Cell.Grey.getValue();
		
		/*Row 3*/
		board[3][0] = Cell.Grey.getValue();
		board[3][1] = Cell.RedFixed.getValue();
		board[3][2] = Cell.Grey.getValue();
		board[3][3] = Cell.Grey.getValue();
		
		return board;
	}

	private static int[][] size6board1(){
		
		int[][] board = new int[6][6];
		
		/*Row 0*/
		board[0][0] = Cell.Grey.getValue();
		board[0][1] = Cell.Grey.getValue();
		board[0][2] = Cell.Grey.getValue();
		board[0][3] = Cell.RedFixed.getValue();
		board[0][4] = Cell.RedFixed.getValue();
		board[0][5] = Cell.Grey.getValue();
		
		/*Row 1*/
		board[1][0] = Cell.Grey.getValue();
		board[1][1] = Cell.RedFixed.getValue();
		board[1][2] = Cell.Grey.getValue();
		board[1][3] = Cell.Grey.getValue();
		board[1][4] = Cell.RedFixed.getValue();
		board[1][5] = Cell.RedFixed.getValue();
		
		/*Row 2*/
		board[2][0] = Cell.Grey.getValue();
		board[2][1] = Cell.Grey.getValue();
		board[2][2] = Cell.Grey.getValue();
		board[2][3] = Cell.Grey.getValue();
		board[2][4] = Cell.Grey.getValue();
		board[2][5] = Cell.Grey.getValue();
		
		/*Row 3*/
		board[3][0] = Cell.Grey.getValue();
		board[3][1] = Cell.YellowFixed.getValue();
		board[3][2] = Cell.Grey.getValue();
		board[3][3] = Cell.RedFixed.getValue();
		board[3][4] = Cell.Grey.getValue();
		board[3][5] = Cell.Grey.getValue();
		
		/*Row 4*/
		board[4][0] = Cell.YellowFixed.getValue();
		board[4][1] = Cell.Grey.getValue();
		board[4][2] = Cell.Grey.getValue();
		board[4][3] = Cell.Grey.getValue();
		board[4][4] = Cell.Grey.getValue();
		board[4][5] = Cell.RedFixed.getValue();
		
		/*Row 5*/
		board[5][0] = Cell.Grey.getValue();
		board[5][1] = Cell.Grey.getValue();
		board[5][2] = Cell.Grey.getValue();
		board[5][3] = Cell.Grey.getValue();
		board[5][4] = Cell.Grey.getValue();
		board[5][5] = Cell.RedFixed.getValue();
		
		return board;
	}

	private static int[][] size6board2(){
		int[][] board = new int[6][6];
		
		/*Row 0*/
		board[0][0] = Cell.Grey.getValue();
		board[0][1] = Cell.Grey.getValue();
		board[0][2] = Cell.Grey.getValue();
		board[0][2] = Cell.Grey.getValue();
		board[0][4] = Cell.Grey.getValue();
		board[0][5] = Cell.Grey.getValue();
		
		/*Row 1*/
		board[1][0] = Cell.Grey.getValue();
		board[1][1] = Cell.Grey.getValue();
		board[1][2] = Cell.Grey.getValue();
		board[1][3] = Cell.Grey.getValue();
		board[1][4] = Cell.YellowFixed.getValue();
		board[1][5] = Cell.Grey.getValue();
		
		/*Row 2*/
		board[2][0] = Cell.Grey.getValue();
		board[2][1] = Cell.Grey.getValue();
		board[2][2] = Cell.YellowFixed.getValue();
		board[2][3] = Cell.Grey.getValue();
		board[2][4] = Cell.Grey.getValue();
		board[2][5] = Cell.RedFixed.getValue();
		
		/*Row 3*/
		board[3][0] = Cell.Grey.getValue();
		board[3][1] = Cell.Grey.getValue();
		board[3][2] = Cell.Grey.getValue();
		board[3][3] = Cell.Grey.getValue();
		board[3][4] = Cell.YellowFixed.getValue();
		board[3][5] = Cell.Grey.getValue();
		
		/*Row 4*/
		board[4][0] = Cell.YellowFixed.getValue();
		board[4][1] = Cell.RedFixed.getValue();
		board[4][2] = Cell.Grey.getValue();
		board[4][3] = Cell.Grey.getValue();
		board[4][4] = Cell.Grey.getValue();
		board[4][5] = Cell.Grey.getValue();
		
		/*Row 5*/
		board[5][0] = Cell.YellowFixed.getValue();
		board[5][1] = Cell.YellowFixed.getValue();
		board[5][2] = Cell.Grey.getValue();
		board[5][3] = Cell.RedFixed.getValue();
		board[5][4] = Cell.Grey.getValue();
		board[5][5] = Cell.Grey.getValue();
		
		return board;
	}

	private static int[][] size8board1(){
		int[][] board = new int[8][8];
		
		/*Row 0*/
		board[0][0] = Cell.YellowFixed.getValue();
		board[0][1] = Cell.Grey.getValue();
		board[0][2] = Cell.Grey.getValue();
		board[0][3] = Cell.Grey.getValue();
		board[0][4] = Cell.RedFixed.getValue();
		board[0][5] = Cell.RedFixed.getValue();
		board[0][6] = Cell.Grey.getValue();
		board[0][7] = Cell.Grey.getValue();
		
		/*Row 1*/
		board[1][0] = Cell.Grey.getValue();
		board[1][1] = Cell.Grey.getValue();
		board[1][2] = Cell.Grey.getValue();
		board[1][3] = Cell.YellowFixed.getValue();
		board[1][4] = Cell.Grey.getValue();
		board[1][5] = Cell.Grey.getValue();
		board[1][6] = Cell.Grey.getValue();
		board[1][7] = Cell.RedFixed.getValue();
		
		/*Row 2*/
		board[2][0] = Cell.Grey.getValue();
		board[2][1] = Cell.YellowFixed.getValue();
		board[2][2] = Cell.Grey.getValue();
		board[2][3] = Cell.Grey.getValue();
		board[2][4] = Cell.Grey.getValue();
		board[2][5] = Cell.Grey.getValue();
		board[2][6] = Cell.YellowFixed.getValue();
		board[2][7] = Cell.Grey.getValue();
		
		/*Row 3*/
		board[3][0] = Cell.Grey.getValue();
		board[3][1] = Cell.Grey.getValue();
		board[3][2] = Cell.Grey.getValue();
		board[3][3] = Cell.Grey.getValue();
		board[3][4] = Cell.Grey.getValue();
		board[3][5] = Cell.Grey.getValue();
		board[3][6] = Cell.Grey.getValue();
		board[3][7] = Cell.RedFixed.getValue();
		
		/*Row 4*/
		board[4][0] = Cell.Grey.getValue();
		board[4][1] = Cell.Grey.getValue();
		board[4][2] = Cell.Grey.getValue();
		board[4][3] = Cell.RedFixed.getValue();
		board[4][4] = Cell.RedFixed.getValue();
		board[4][5] = Cell.Grey.getValue();
		board[4][6] = Cell.Grey.getValue();
		board[4][7] = Cell.Grey.getValue();
		
		/*Row 5*/
		board[5][0] = Cell.Grey.getValue();
		board[5][1] = Cell.Grey.getValue();
		board[5][2] = Cell.Grey.getValue();
		board[5][3] = Cell.Grey.getValue();
		board[5][4] = Cell.RedFixed.getValue();
		board[5][5] = Cell.Grey.getValue();
		board[5][6] = Cell.Grey.getValue();
		board[5][7] = Cell.Grey.getValue();
		
		/*Row 6*/
		board[6][0] = Cell.Grey.getValue();
		board[6][1] = Cell.Grey.getValue();
		board[6][2] = Cell.Grey.getValue();
		board[6][3] = Cell.Grey.getValue();
		board[6][4] = Cell.Grey.getValue();
		board[6][5] = Cell.Grey.getValue();
		board[6][6] = Cell.RedFixed.getValue();
		board[6][7] = Cell.RedFixed.getValue();
		
		/*Row 7*/
		board[7][0] = Cell.RedFixed.getValue();
		board[7][1] = Cell.Grey.getValue();
		board[7][2] = Cell.Grey.getValue();
		board[7][3] = Cell.Grey.getValue();
		board[7][4] = Cell.Grey.getValue();
		board[7][5] = Cell.Grey.getValue();
		board[7][6] = Cell.Grey.getValue();
		board[7][7] = Cell.RedFixed.getValue();		
		
		return board;
	}
	
	private static int[][] size8board2(){
		int board[][] = new int[8][8];
		
		/*Row 0*/
		board[0][0] = Cell.Grey.getValue();
		board[0][1] = Cell.Grey.getValue();
		board[0][2] = Cell.YellowFixed.getValue();
		board[0][3] = Cell.Grey.getValue();
		board[0][4] = Cell.Grey.getValue();
		board[0][5] = Cell.RedFixed.getValue();
		board[0][6] = Cell.Grey.getValue();
		board[0][7] = Cell.YellowFixed.getValue();
		
		/*Row 1*/
		board[1][0] = Cell.Grey.getValue();
		board[1][1] = Cell.Grey.getValue();
		board[1][2] = Cell.Grey.getValue();
		board[1][3] = Cell.YellowFixed.getValue();
		board[1][4] = Cell.Grey.getValue();
		board[1][5] = Cell.Grey.getValue();
		board[1][6] = Cell.Grey.getValue();
		board[1][7] = Cell.YellowFixed.getValue();
		
		/*Row 2*/
		board[2][0] = Cell.Grey.getValue();
		board[2][1] = Cell.YellowFixed.getValue();
		board[2][2] = Cell.Grey.getValue();
		board[2][3] = Cell.YellowFixed.getValue();
		board[2][4] = Cell.Grey.getValue();
		board[2][5] = Cell.Grey.getValue();
		board[2][6] = Cell.Grey.getValue();
		board[2][7] = Cell.Grey.getValue();
		
		/*Row 3*/
		board[3][0] = Cell.RedFixed.getValue();
		board[3][1] = Cell.Grey.getValue();
		board[3][2] = Cell.Grey.getValue();
		board[3][3] = Cell.Grey.getValue();
		board[3][4] = Cell.Grey.getValue();
		board[3][5] = Cell.RedFixed.getValue();
		board[3][6] = Cell.Grey.getValue();
		board[3][7] = Cell.Grey.getValue();
		
		/*Row 4*/
		board[4][0] = Cell.RedFixed.getValue();
		board[4][1] = Cell.Grey.getValue();
		board[4][2] = Cell.Grey.getValue();
		board[4][3] = Cell.Grey.getValue();
		board[4][4] = Cell.Grey.getValue();
		board[4][5] = Cell.Grey.getValue();
		board[4][6] = Cell.Grey.getValue();
		board[4][7] = Cell.Grey.getValue();
		
		/*Row 5*/
		board[5][0] = Cell.Grey.getValue();
		board[5][1] = Cell.Grey.getValue();
		board[5][2] = Cell.Grey.getValue();
		board[5][3] = Cell.RedFixed.getValue();
		board[5][4] = Cell.Grey.getValue();
		board[5][5] = Cell.YellowFixed.getValue();
		board[5][6] = Cell.Grey.getValue();
		board[5][7] = Cell.Grey.getValue();
		
		/*Row 6*/
		board[6][0] = Cell.RedFixed.getValue();
		board[6][1] = Cell.Grey.getValue();
		board[6][2] = Cell.Grey.getValue();
		board[6][3] = Cell.Grey.getValue();
		board[6][4] = Cell.Grey.getValue();
		board[6][5] = Cell.YellowFixed.getValue();
		board[6][6] = Cell.Grey.getValue();
		board[6][7] = Cell.Grey.getValue();
		
		/*Row 7*/
		board[7][0] = Cell.Grey.getValue();
		board[7][1] = Cell.YellowFixed.getValue();
		board[7][2] = Cell.Grey.getValue();
		board[7][3] = Cell.Grey.getValue();
		board[7][4] = Cell.YellowFixed.getValue();
		board[7][5] = Cell.Grey.getValue();
		board[7][6] = Cell.Grey.getValue();
		board[7][7] = Cell.Grey.getValue();	
		
		return board;
	}
}
