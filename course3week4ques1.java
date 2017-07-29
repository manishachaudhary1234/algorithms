import java.io.BufferedReader;
import java.io.DataInputStream;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

/**
 * Algorithms: Design and Analysis, Part 2
 * Programming Question - Week 3
 * @author Felix Garcia Lainez
 */
public class Question1
{
    private static int n = 0; //number of items
    private static int w = 0; //knapsack size
    private static ArrayList<KnapsackItem> itemsArray = new ArrayList<KnapsackItem>();
    
    /**
     * @param args
     */
    public static void main(String[] args) 
    {
        //Load data from file
        loadDataFromFile();
        
        //Initialization
        int[][] A = new int[n + 1][w + 1];
        
        for(int j = 0; j <= w; j++){
            A[0][j] = 0;
        }
        
        //Main Loop
        for(int i = 1; i <= n; i++)
        {
            KnapsackItem currentItem = itemsArray.get(i - 1);
            
            for(int x = 0; x <= w; x++)
            {
                int firstItem = A[i - 1][x];
                
                int secondItem = 0;
    
                if(x - currentItem.getWeight() >= 0 && x - currentItem.getWeight() <= w){
                    secondItem = A[i - 1][x - currentItem.getWeight()] + currentItem.getValue();
                }
                
                A[i][x] = Math.max(firstItem, secondItem);
            }
        }
        
        System.out.println("*** Optimal Solution => " + A[n][w] + " ***");
    }
    
    /**
     * Load the data of the problem from a given file
     */
    private static void loadDataFromFile()
    {
        try
        {
            FileInputStream f = new FileInputStream("knapsack1.txt");
            DataInputStream d = new DataInputStream(f);
            BufferedReader b =  new BufferedReader(new InputStreamReader(d));
            
            StringTokenizer tokenizer = new StringTokenizer(b.readLine());
 
            w = Integer.parseInt(tokenizer.nextToken());
            n = Integer.parseInt(tokenizer.nextToken());
            
            int value;
            int weight;
            String str;
            
            while((str=b.readLine())!=null)
            {
                tokenizer = new StringTokenizer(str);
                
		value = Integer.parseInt(tokenizer.nextToken());
		weight = Integer.parseInt(tokenizer.nextToken());

                itemsArray.add(new KnapsackItem(value, weight));
            }
        }
        catch(Exception ex){
        } 
    }
}
