import java.io.*;

public class MedianMaintenance {
	
	public static void main(String[] args){
		int median = 0; 
		int sumMedian = 0; 
		try{
			BufferedReader rd = new BufferedReader(new FileReader(FILENAME));
			while(true){
				String line = rd.readLine();
				if(line == null) break;
				median = findMedian(Integer.parseInt(line));
				sumMedian += median;
			}	
		}
		catch(IOException ex){
			System.out.println("Cannot find the file \"" + FILENAME + "\"");
			System.exit(0);
		}
		System.out.println("the sum is: " + sumMedian);
	}
	
	private static int findMedian(int input){
		if(input < minHeap.getMin()) {
			maxHeap.insert(input);
		} else{
			minHeap.insert(input);
		}
		if(maxHeap.getSize() - minHeap.getSize() > 1){
			minHeap.insert(maxHeap.extractMax());
		}
		if(minHeap.getSize() > maxHeap.getSize()){
			maxHeap.insert(minHeap.extractMin());
		}
		return maxHeap.getMax();
	}

	private static final String FILENAME = "file/Median.txt";
	private static MaxHeap maxHeap = new MaxHeap(); 
	private static MinHeap minHeap = new MinHeap();
	
}
