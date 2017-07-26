mport static java.util.Collections.sort;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

public class Main {
  
  public static void main(String[] args) throws FileNotFoundException {
    Scanner in = new Scanner(new File("SCC.txt"));
    Graph graph = new Graph();
    while (in.hasNext()) {
      graph.addEdge(in.nextInt(), in.nextInt());
    }
    List<Integer> sccSizes = graph.getSCCSizes();
    sort(sccSizes);
    for (Integer size : sccSizes) {
      System.out.println(size);
    }
  }
  public static class Graph {
    HashMap<Integer, Node> nodes;
    
    public Graph() {
      nodes = new HashMap<Integer, Node>();
    }
    
    public List<Integer> getSCCSizes() {
      int n = nodes.size();
      List<Node> list = new ArrayList<Node>(n);
      for (Node node : nodes.values()) {
        node.visitBackwards(list);
      }
      List<Integer> sccSizes = new LinkedList<Integer>();
      while (0 < n--) {
        sccSizes.add(list.get(n).countReachableNonVisitedComponents());
      }
      return sccSizes; 
    }

    void addEdge(int fromId, int toId) {
      Node from = nodes.get(fromId);
      if (null == from) {
        from = new Node(fromId);
        nodes.put(fromId, from);
      }
      Node to = nodes.get(toId);
      if (null == to) {
        to = new Node(toId);
        nodes.put(toId, to);
      }
      from.addTo(to);
      to.addFrom(from);
    }
    
    class Node {
      boolean visitedBackwards;
      boolean visited;
      List<Node> from;
      List<Node> to;
      
      Node(int id) {
        from = new LinkedList<Node>();
        to = new LinkedList<Node>();
      }
      
      public int countReachableNonVisitedComponents() {
        if (visited) {
          return 0;
        }
        visited = true;
        int count = 0;
        for (Node node : to) {
          count += node.countReachableNonVisitedComponents();
        }
        return 1 + count;
      }
      
      public void visitBackwards(List<Node> list) {
        if (visitedBackwards) {
          return;
        }
        visitedBackwards = true;
        for (Node node : from) {
          node.visitBackwards(list);
        }
        list.add(this);
      }

      void addTo(Node to) {
        this.to.add(to);
      }
      
      void addFrom(Node from) {
        this.from.add(from);
      }
    }
  }
}
