package gps.common;

public class ColumnState {
    public final int swaps;
    public final int countRed;
    public final int countYellow;

    public ColumnState(int swaps, int countRed, int countYellow) {
        this.swaps = swaps;
        this.countRed = countRed;
        this.countYellow = countYellow;
    }
}