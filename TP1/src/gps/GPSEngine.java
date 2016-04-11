package gps;

import gps.api.GPSProblem;
import gps.api.GPSRule;
import gps.api.GPSState;
import gps.exception.NotAppliableException;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Queue;

public abstract class GPSEngine {

//	protected Queue<GPSNode> open;
	protected Map<GPSState, Integer> bestCosts = new HashMap<GPSState, Integer>();

	private List<GPSNode> open = new LinkedList<GPSNode>();
	private List<GPSNode> closed = new ArrayList<GPSNode>();

	protected GPSProblem problem;

	// Use this variable in open set order.
	protected SearchStrategy strategy;

	private int generatedCounter = 0;
	public void engine(GPSProblem myProblem, SearchStrategy myStrategy) {

		problem = myProblem;
		strategy = myStrategy;

		long startTime = System.currentTimeMillis();

		GPSNode rootNode = new GPSNode(problem.getInitState(), 0);
		boolean finished = false;
		boolean failed = false;
		long explosionCounter = 0;
		open.add(rootNode);
		while (!failed && !finished) {
			if (open.size() <= 0) {
				failed = true;
			} else {
				GPSNode currentNode = open.get(0);
				closed.add(currentNode);
				open.remove(0);
				if (problem.isGoal(currentNode.getState())) {
					long endTime = System.currentTimeMillis();
					finished = true;
					System.out.println(currentNode.getSolution());
					System.out.println("Expanded nodes: " + explosionCounter);
					System.out.println("Generated nodes: " + generatedCounter);
					System.out.println("Solution cost: " + currentNode.getCost());
					System.out.println("Border nodes: " + open.size());
					float seconds = (float) (((endTime - startTime) / 1000.0) % 60.0);
					String formattedSeconds = String.format("%.02f", seconds);
					System.out.println("Execution time: " + (endTime - startTime) + " milliseconds ("+ formattedSeconds +" seconds)");
				} else {
					explosionCounter++;
					explode(currentNode);
				}
			}
		}
		if (finished) {
			System.out.println("OK! solution found!");
		} else if (failed) {
			System.err.println("FAILED! solution not found!");
		}
	}

	private  boolean explode(GPSNode node) {
		if(problem.getRules() == null){
			System.err.println("No rules!");
			return false;
		}

		for (GPSRule rule : problem.getRules()) {
			GPSState newState = null;
			try {
				newState = rule.evalRule(node.getState());
			} catch (NotAppliableException e) {
				// Do nothing
			}
			if (newState != null
					&& !checkBranch(node, newState)
					&& !checkOpenAndClosed(node.getCost() + rule.getCost(),
							newState)) {
				GPSNode newNode = new GPSNode(newState, node.getCost()
						+ rule.getCost());
				newNode.setParent(node);
				addNode(newNode);
				generatedCounter++;
			}
		}
		return true;
	}
	
	private  boolean checkOpenAndClosed(Integer cost, GPSState state) {
		for (GPSNode openNode : open) {
			if (openNode.getState().equals(state) && openNode.getCost() <= cost) {
				return true;
			}
		}
		for (GPSNode closedNode : closed) {
			if (closedNode.getState().equals(state)
					&& closedNode.getCost() <= cost) {
				return true;
			}
		}
		return false;
	}

	private  boolean checkBranch(GPSNode parent, GPSState state) {
		if (parent == null) {
			return false;
		}
		return checkBranch(parent.getParent(), state)
				|| state.equals(parent.getState());
	}
	
//	private boolean explode(GPSNode node) {
//		if(bestCosts.containsKey(node.getState()) && bestCosts.get(node.getState()) <= node.getCost()){
//			return false;
//		}
//		updateBest(node);
//		if (problem.getRules() == null) {
//			System.err.println("No rules!");
//			return false;
//		}
//		for (GPSRule rule : problem.getRules()) {
//			GPSState newState = null;
//			try {
//				newState = rule.evalRule(node.getState());
//			} catch (NotAppliableException e) {
//				// Do nothing
//			}
//			if (newState != null && isBest(newState, node.getCost() + rule.getCost())) {
//				GPSNode newNode = new GPSNode(newState, node.getCost() + rule.getCost());
//				newNode.setParent(node);
////				open.add(newNode);
//				addNode(newNode);
//			}
//		}
//		return true;
//	}

//	private boolean isBest(GPSState state, Integer cost) {
//		return !bestCosts.containsKey(state) || cost < bestCosts.get(state);
//	}
//
//	private void updateBest(GPSNode node) {
//		bestCosts.put(node.getState(), node.getCost());
//	}

	public SearchStrategy getStrategy() {
		return strategy;
	}
	
	public List<GPSNode> getOpen() {
		return open;
	}

	public List<GPSNode> getClosed() {
		return closed;
	}
	
	public void resetClosedNode() {
		this.closed.clear();
	}
	
	public GPSProblem getProblem() {
		return problem;
	}	
	public abstract  void addNode(GPSNode node);

}


