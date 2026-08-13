import java.util.ArrayList;

public class Solution {


    static void main(String[] args){
        // 
        int [][] edges = {{0,2},{0,1},{1,2},{2,3}};
        int v = 4;

        // Make a adj List
        ArrayList<ArrayList<Integer>> adjList = new ArrayList<>();
        
        for (int i = 0 ; i < v ; i++){
            adjList.add(new ArrayList<>());
        }

        for (int i = 0 ; i < edges.length ; i++){
            int u = edges[i][0];
            int p = edges[i][1];
            adjList.get(u).add(p);
            adjList.get(p).add(u);
        }

    }
}
