package ohh1.gps.api;
import java.util.List;

import gps.GPSEngine;
import gps.GPSNode;
import gps.SearchStrategy;

public class Ohh1Engine extends GPSEngine {

	int depth = 0;
	GPSNode nodeRoot = null;

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

				while (i < openSize
						&& this.getOpen().get(i).getParent()
								.equals(node.getParent())) {
					i++;
				}

				this.getOpen().add(i, node);
			}
		}

		if (this.getStrategy().equals(SearchStrategy.IDDFS)) {
			//cuando agrego el primero nodo, que es hijo del
			//nodo raiz, me guardo la raiz.
			if (this.getOpen().size() == 0) {
				nodeRoot = node.getParent();
				depth++;
//				System.out.println("profundidad: "+ depth);
			}

			if (!this.getOpen().isEmpty() && this.getOpen().get(0).equals(nodeRoot)){
				if(!this.getClosed().isEmpty()){
					this.resetClosedNode();
				}
				return;
			}


			int index = 0;
			boolean foundParent = false;
			if (node.getCost() <= depth) {
				for (; !foundParent && index < this.getOpen().size(); index++) {
					if (node.getParent().equals(this.getOpen().get(index))) {
						foundParent = true;
					}
				}

				boolean lastBrother = false;
				for (; !lastBrother && index < this.getOpen().size(); index++) {
					if (!node.getParent().equals(this.getOpen().get(index))) {
						lastBrother = true;
					}
				}
				
				this.getOpen().add(index, node);
			} else {
				//vuelvo a poner el nodo raiz para volver a recorrer
				//los estados.
				if (!this.getOpen().contains(nodeRoot)){
					this.getOpen().add(nodeRoot);
				}
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
