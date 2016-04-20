package gps.common;

public class BoardSelector {
	
	public static int OPTION = 1;
	
	public static int[][] Selector(int size){
		
	
		switch(size){
			case 4: return OPTION == 1 ? size4board1() : size4board2();
			case 6: 
					switch(OPTION){
						case 1: return size6board1();
						case 2: return size6board2();
						case 3: return size6board3();
						case 4: return size6board4();
						case 5: return size6board5();
						default: return null;
					}
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
		board[0][1] = Cell.RedFixed.getValue();
		board[0][2] = Cell.Grey.getValue();
		board[0][3] = Cell.Grey.getValue();
		board[0][4] = Cell.Grey.getValue();
		board[0][5] = Cell.Grey.getValue();
		
		/*Row 1*/
		board[1][0] = Cell.Grey.getValue();
		board[1][1] = Cell.YellowFixed.getValue();
		board[1][2] = Cell.Grey.getValue();
		board[1][3] = Cell.Grey.getValue();
		board[1][4] = Cell.Grey.getValue();
		board[1][5] = Cell.Grey.getValue();
		
		/*Row 2*/
		board[2][0] = Cell.RedFixed.getValue();
		board[2][1] = Cell.Grey.getValue();
		board[2][2] = Cell.Grey.getValue();
		board[2][3] = Cell.Grey.getValue();
		board[2][4] = Cell.YellowFixed.getValue();
		board[2][5] = Cell.Grey.getValue();
		
		/*Row 3*/
		board[3][0] = Cell.YellowFixed.getValue();
		board[3][1] = Cell.YellowFixed.getValue();
		board[3][2] = Cell.Grey.getValue();
		board[3][3] = Cell.Grey.getValue();
		board[3][4] = Cell.Grey.getValue();
		board[3][5] = Cell.Grey.getValue();
		
		/*Row 4*/
		board[4][0] = Cell.Grey.getValue();
		board[4][1] = Cell.RedFixed.getValue();
		board[4][2] = Cell.Grey.getValue();
		board[4][3] = Cell.Grey.getValue();
		board[4][4] = Cell.Grey.getValue();
		board[4][5] = Cell.RedFixed.getValue();
		
		/*Row 5*/
		board[5][0] = Cell.Grey.getValue();
		board[5][1] = Cell.Grey.getValue();
		board[5][2] = Cell.YellowFixed.getValue();
		board[5][3] = Cell.Grey.getValue();
		board[5][4] = Cell.Grey.getValue();
		board[5][5] = Cell.Grey.getValue();
		
		return board;
	}
	
	private static int[][] size6board3(){
		int[][] board = new int[6][6];
		
		/*Row 0*/
		board[0][0] = Cell.Grey.getValue();
		board[0][1] = Cell.Grey.getValue();
		board[0][2] = Cell.YellowFixed.getValue();
		board[0][3] = Cell.Grey.getValue();
		board[0][4] = Cell.YellowFixed.getValue();
		board[0][5] = Cell.RedFixed.getValue();
		
		/*Row 1*/
		board[1][0] = Cell.YellowFixed.getValue();
		board[1][1] = Cell.YellowFixed.getValue();
		board[1][2] = Cell.Grey.getValue();
		board[1][3] = Cell.Grey.getValue();
		board[1][4] = Cell.Grey.getValue();
		board[1][5] = Cell.Grey.getValue();
		
		/*Row 2*/
		board[2][0] = Cell.Grey.getValue();
		board[2][1] = Cell.Grey.getValue();
		board[2][2] = Cell.YellowFixed.getValue();
		board[2][3] = Cell.Grey.getValue();
		board[2][4] = Cell.Grey.getValue();
		board[2][5] = Cell.Grey.getValue();
		
		/*Row 3*/
		board[3][0] = Cell.Grey.getValue();
		board[3][1] = Cell.Grey.getValue();
		board[3][2] = Cell.YellowFixed.getValue();
		board[3][3] = Cell.Grey.getValue();
		board[3][4] = Cell.Grey.getValue();
		board[3][5] = Cell.Grey.getValue();
		
		/*Row 4*/
		board[4][0] = Cell.Grey.getValue();
		board[4][1] = Cell.RedFixed.getValue();
		board[4][2] = Cell.Grey.getValue();
		board[4][3] = Cell.Grey.getValue();
		board[4][4] = Cell.Grey.getValue();
		board[4][5] = Cell.Grey.getValue();
		
		/*Row 5*/
		board[5][0] = Cell.YellowFixed.getValue();
		board[5][1] = Cell.Grey.getValue();
		board[5][2] = Cell.Grey.getValue();
		board[5][3] = Cell.Grey.getValue();
		board[5][4] = Cell.Grey.getValue();
		board[5][5] = Cell.Grey.getValue();
		
		return board;
	}
	
	private static int[][] size6board4(){
		int[][] board = new int[6][6];
		
		/*Row 0*/
		board[0][0] = Cell.Grey.getValue();
		board[0][1] = Cell.Grey.getValue();
		board[0][2] = Cell.Grey.getValue();
		board[0][3] = Cell.Grey.getValue();
		board[0][4] = Cell.Grey.getValue();
		board[0][5] = Cell.Grey.getValue();
		
		/*Row 1*/
		board[1][0] = Cell.YellowFixed.getValue();
		board[1][1] = Cell.Grey.getValue();
		board[1][2] = Cell.Grey.getValue();
		board[1][3] = Cell.Grey.getValue();
		board[1][4] = Cell.Grey.getValue();
		board[1][5] = Cell.Grey.getValue();
		
		/*Row 2*/
		board[2][0] = Cell.Grey.getValue();
		board[2][1] = Cell.Grey.getValue();
		board[2][2] = Cell.Grey.getValue();
		board[2][3] = Cell.RedFixed.getValue();
		board[2][4] = Cell.Grey.getValue();
		board[2][5] = Cell.Grey.getValue();
		
		/*Row 3*/
		board[3][0] = Cell.Grey.getValue();
		board[3][1] = Cell.RedFixed.getValue();
		board[3][2] = Cell.Grey.getValue();
		board[3][3] = Cell.Grey.getValue();
		board[3][4] = Cell.YellowFixed.getValue();
		board[3][5] = Cell.Grey.getValue();
		
		/*Row 4*/
		board[4][0] = Cell.YellowFixed.getValue();
		board[4][1] = Cell.Grey.getValue();
		board[4][2] = Cell.Grey.getValue();
		board[4][3] = Cell.Grey.getValue();
		board[4][4] = Cell.Grey.getValue();
		board[4][5] = Cell.YellowFixed.getValue();
		
		/*Row 5*/
		board[5][0] = Cell.YellowFixed.getValue();
		board[5][1] = Cell.Grey.getValue();
		board[5][2] = Cell.Grey.getValue();
		board[5][3] = Cell.Grey.getValue();
		board[5][4] = Cell.Grey.getValue();
		board[5][5] = Cell.Grey.getValue();
		
		return board;
	}
	
	private static int[][] size6board5(){
		int[][] board = new int[6][6];
		
		/*Row 0*/
		board[0][0] = Cell.Grey.getValue();
		board[0][1] = Cell.RedFixed.getValue();
		board[0][2] = Cell.Grey.getValue();
		board[0][3] = Cell.Grey.getValue();
		board[0][4] = Cell.Grey.getValue();
		board[0][5] = Cell.Grey.getValue();
		
		/*Row 1*/
		board[1][0] = Cell.Grey.getValue();
		board[1][1] = Cell.Grey.getValue();
		board[1][2] = Cell.Grey.getValue();
		board[1][3] = Cell.YellowFixed.getValue();
		board[1][4] = Cell.Grey.getValue();
		board[1][5] = Cell.YellowFixed.getValue();
		
		/*Row 2*/
		board[2][0] = Cell.Grey.getValue();
		board[2][1] = Cell.Grey.getValue();
		board[2][2] = Cell.YellowFixed.getValue();
		board[2][3] = Cell.Grey.getValue();
		board[2][4] = Cell.Grey.getValue();
		board[2][5] = Cell.Grey.getValue();
		
		/*Row 3*/
		board[3][0] = Cell.Grey.getValue();
		board[3][1] = Cell.YellowFixed.getValue();
		board[3][2] = Cell.Grey.getValue();
		board[3][3] = Cell.Grey.getValue();
		board[3][4] = Cell.YellowFixed.getValue();
		board[3][5] = Cell.Grey.getValue();
		
		/*Row 4*/
		board[4][0] = Cell.Grey.getValue();
		board[4][1] = Cell.Grey.getValue();
		board[4][2] = Cell.Grey.getValue();
		board[4][3] = Cell.Grey.getValue();
		board[4][4] = Cell.YellowFixed.getValue();
		board[4][5] = Cell.Grey.getValue();
		
		/*Row 5*/
		board[5][0] = Cell.YellowFixed.getValue();
		board[5][1] = Cell.RedFixed.getValue();
		board[5][2] = Cell.Grey.getValue();
		board[5][3] = Cell.Grey.getValue();
		board[5][4] = Cell.Grey.getValue();
		board[5][5] = Cell.YellowFixed.getValue();
		
		return board;
	}

	
	

}
