
#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n ;
    cin >> n;
    for(int i = 0 ; i <= n/2 ; i++){
        // print spaces
        int count = n/2 - i;
        for(int space = 0 ; space < count ; space++)
        cout << " ";
        // print number
        
        for(int k = 1 ; k <= i + 1 ; k++){
            cout << k;
            if( k != i + 1)
            cout << "*";
        }
        
        // again print spaces
        
        for(int space = 0 ; space < count ; space++)
        cout << " ";
        cout << endl;
    }
    // printing second half
    
    for(int i = n/2 + 1 ; i < n ; i++ ){
        int count = i - n/2;
        for(int space = 0 ; space < count ; space++)
        cout << " ";
        // print number
        
        for(int k = 1 ; k <= n-i ; k++){
            cout << k;
            if( k != n - i)
            cout << "*";
        }
        
        // again print spaces
        
        for(int space = 0 ; space < count ; space++)
        cout << " ";
        cout << endl;
    }
    
    
    return 0;
}