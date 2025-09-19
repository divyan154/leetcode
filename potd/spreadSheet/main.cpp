class Spreadsheet {
    unordered_map<string,int> mpp;
public:

    Spreadsheet(int rows) {
       
    }
    
    void setCell(string cell, int value) {
        mpp[cell] = value;
    }
    
    void resetCell(string cell) {
        mpp[cell] = 0;
    }
    
    int getValue(string formula) {
        int plusPos = formula.find("+");
        string leftStr = formula.substr(1,plusPos-1);
        string rightStr = formula.substr(plusPos+1);
        int lvalue = (leftStr[0] >= 'A' && leftStr[0] <= 'Z') ? mpp[leftStr]:stoi(leftStr);
        int rvalue = (rightStr[0] >= 'A' && rightStr[0] <= 'Z') ? mpp[rightStr]:stoi(rightStr);
        return lvalue + rvalue;
    }
};

/**
 * Your Spreadsheet object will be instantiated and called as such:
 * Spreadsheet* obj = new Spreadsheet(rows);
 * obj->setCell(cell,value);
 * obj->resetCell(cell);
 * int param_3 = obj->getValue(formula);
 */