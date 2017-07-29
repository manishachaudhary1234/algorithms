
import java.io.BufferedReader;
import java.io.DataInputStream;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.StringTokenizer;

/**
 * Algorithms: Design and Analysis, Part 2
 * Programming Question - Week 3
 * @author Felix Garcia Lainez
 */
public class Question2
{
    private static int n = 0; //Number of items
    private static int w = 0; //Knapsack size
    private static ArrayList<KnapsackItem> itemsArray = new ArrayList<KnapsackItem>();
    
    //Used to cache results and improve performance, decreasing 
    //the number of recursive calls required to do the computation
    private static HashMap<String, Integer> cache = new HashMap<String, Integer>();
    
    /**
     * @param args
     */
    public static void main(String[] args) 
    {
        //Load data from file
        loadDataFromFile();
        
        //Recursive Implementation
        System.out.println("*** Optimal Solution => " + processKnapsack(itemsArray.size() - 1, w) + " ***");
    }
    
    /**
     * Recursive method
     */
    private static int processKnapsack(int i, int w)
    {
        //Read solution from cache
        int solution = getSolutionFromCache(i, w);
        
        //If the solution for the values i and w doesn't exists then compute it recursively
        if(solution == -1)
        {
            if(i < 0){
                return 0;
            }
        
            KnapsackItem currentItem = itemsArray.get(i);
    
            if(currentItem.getWeight() > w){
                solution = processKnapsack(i - 1, w);
            }
            else{
                solution = Math.max(processKnapsack(i - 1, w), processKnapsack(i - 1, w - currentItem.getWeight()) + currentItem.getValue());   
            }
        
            //Save the calculated solution in the cache
            saveSolutionInChache(i, w, solution);
        }   
            
        return solution;
    }
    
    /**
     * Saves the calculated solution in cache
     * @param i Used to create the key to store the solution in the HashMap
     * @param w Used to create the key to store the solution in the HashMap
     * @param solution The solution to be stored in the HashMap
     */
    private static void saveSolutionInChache(int i, int w, int solution){
        cache.put("Item" + i + ":" + w, solution);
    }
    
    /**
     * Get a calculated solution from cache
     * @param i Used to create the key to get the solution stored in the HashMap
     * @param w Used to create the key to get the solution stored in the HashMap
     * @return The solution if exits, else -1
     */
    private static int getSolutionFromCache(int i, int w)
    {
        int cachedSolution = -1;
        String key = "Item" + i + ":" + w;
        
        if(cache.containsKey(key)){
            cachedSolution = cache.get(key);
        }
        
        return cachedSolution;
    }
    
    /**
     * Load the data of the problem from a given file
     */
    private static void loadDataFromFile()
    {
        try
        {
            FileInputStream f = new FileInputStream("knapsack_big.txt");
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
