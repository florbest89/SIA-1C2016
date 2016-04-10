package ohh1.gps.api;

import java.util.Comparator;
import java.util.PriorityQueue;

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
		
		if (this.getStrategy().equals(SearchStrategy.GREEDY)){
			  if (!this.getOpen().isEmpty()) {
			    
			    int i = 0;
			    
			    //Save H value of current node 
			    int hValueCurrent = this.getProblem().getHValue(node.getState());

			    //Iterate the open node list to find nodes with the same parent
			    while (i < this.getOpen().size() && this.getOpen().get(i).getParent().equals(node.getParent())) {

			      int hValueLocal = this.getProblem().getHValue(this.getOpen().get(i).getState());

			      //Compare current H value to add the node the correct order.
			      if (hValueCurrent < hValueLocal) {
			        this.getOpen().add(i, node);
			        return;
			      }

			      i++;
			    }

			    if (i == this.getOpen().size()) {
			      this.getOpen().add(node);
			      return;
			    }

			    this.getOpen().add(i, node);
			    
			  } else {
				  
			    this.getOpen().add(node);
			    
			  }
		}
		
		if (this.getStrategy().equals(SearchStrategy.ASTAR)){
			if (!this.getOpen().isEmpty()) {
		        
			    int hValue = getProblem().getHValue(node.getState());
			    int fValue = hValue + node.getCost();

			    for (int i = 0; i < this.getOpen().size(); i++) {

			      GPSNode aNode = this.getOpen().get(i);

			      int fValueOther = this.getProblem().getHValue(aNode.getState()) + aNode.getCost();

			      if (fValue == fValueOther) {

			        if (hValue < this.getProblem().getHValue(aNode.getState())) {

			          this.getOpen().add(i, node);
			          return;
			        }

			      } else {

			        if (fValue < fValueOther) {
			          this.getOpen().add(i, node);
			          return;
			        }
			      }
			    }

			    this.getOpen().add(node);

			  } else {

			    this.getOpen().add(node);
			  }
		}
	}
}
