// time complexity - O(N^2) , less efficient
// uses swapping to sort , put individual elements to their correct position 
// here we find the min_element and put it in starting position 
class Solution {
  public:
    // Function to perform selection sort on the given array.
    void selectionSort(vector<int> &arr) {
        
        int n = arr.size();
        int min_ind = 0;
        for(int i = 0 ; i < n-1 ; i++){
            min_ind = i;
            
            for(int j = i+1 ; j < n ; j++){
                if(arr[min_ind] > arr[j])
                min_ind = j;
            } 
            
            //
            swap(arr[i],arr[min_ind]);
        }
        
    }
};