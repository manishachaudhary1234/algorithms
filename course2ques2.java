import java.io.*;
import java.util.*;

public class Graph {
	
	private ArrayList<ArrayList<int[]>> vertices; 
	private HashSet<Integer> explored; 
	
	public Graph(String inputFileName) throws FileNotFoundException{
		vertices = new ArrayList<ArrayList<int[]>>();
		Scanner in = new Scanner(new File(inputFileName));
		//add all vertices
		while (in.hasNextLine()){
			 vertices.add(new ArrayList<int[]>());
			 String[] line = in.nextLine().split("\t");
			 int node = Integer.parseInt(line[0]);
			 for (int i = 1; i < line.length; i++){
				 String[] edgeStr = line[i].split(",");
				 int[] edge = new int[2];
				 edge[0] = Integer.parseInt(edgeStr[0]);
				 edge[1] = Integer.parseInt(edgeStr[1]);
				 vertices.get(node - 1).add(edge);
			 }
		}		
	}
	
	public int[] shortestPath(){
		int n = vertices.size();
		explored = new HashSet<Integer>();
		int[] paths = new int[n];
		explored.add(1);
		paths[0] = 0;
		while (explored.size() < n){
			int w = -1;
			int l = 1000000;
			for (int node : explored){				
				for (int[] edge : vertices.get(node - 1)){
					if (!explored.contains(edge[0])){
						if (paths[node-1] + edge[1] < l){
							w = edge[0];
							l = paths[node-1] + edge[1];
						}
					}
				}
			}
			if (w != -1){
				explored.add(w);
				paths[w-1] = l;
			} else {
				for (int i = 0; i < n; i++){
					if (!explored.contains(i+1)){
						paths[i] = 1000000;
					}
				}
				break;
			}
		}		
		return paths;
	}
	
	public static void main(String[] args) throws FileNotFoundException{
		Graph g = new Graph("DijkstraData.txt");
		int[] paths = g.shortestPath();	
		System.out.println(paths[6] + "," + paths[36] + "," + paths[58] + "," + 
						   paths[81] + "," + paths[98] + "," + paths[114] + "," + 
						   paths[132] + "," + paths[164] + "," + paths[187] + 
						   "," + paths[196]);
}
