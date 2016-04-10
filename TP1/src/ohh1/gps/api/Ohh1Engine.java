package ohh1.gps.api;
import gps.GPSEngine;
import gps.GPSNode;
import gps.SearchStrategy;

public class Ohh1Engine extends GPSEngine {

//	public Ohn1Engine() {
//		open = new PriorityQueue<GPSNode>(new Comparator<GPSNode>() {
//			@Override
//			public int compare(GPSNode o1, GPSNode o2) {
//				switch (strategy) {
//				case BFS:
//					return o1.getCost() - o2.getCost();
//				case DFS:
//					return o2.getCost() - o1.getCost();
//				default:
//					return 0;
//				}
//			}
//		});
//	}

	
	@Override
	public void addNode(GPSNode node) {

		if (this.getStrategy().equals(SearchStrategy.BFS)) {
			this.getOpen().add(node);
		}

		if (this.getStrategy().equals(SearchStrategy.DFS)) {
			int openSize = this.getOpen().size();
			if (openSize == 0) {

				this.getOpen().add(node);

			} else {

				int i = 0;

				while (i < openSize && this.getOpen().get(i).getParent().equals(node.getParent())) {
					i++;
				}

				this.getOpen().add(i, node);
			}

		}
	}
}
