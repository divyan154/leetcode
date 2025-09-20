class Router {
    private:
    long long encode(int source, int destination, int timestamp){
        return ((long long) source << 40) | ((long long) destination << 20) | timestamp;

    }
    unordered_map<long long,vector<int>>packets;// for storing encoded key --> vector of packets
    queue<long long> q;  // storing keys in queue
    unordered_map<int,vector<int>> timeStamps; // for storing destination --> vector of timeStamps
    int maxSize;
public:
    Router(int memoryLimit) {
        maxSize = memoryLimit;
    }
    
    bool addPacket(int source, int destination, int timestamp) {
        long long key = encode(source,destination, timestamp);
        if(packets.find(key) != packets.end())
        return false;

        if(q.size() >= maxSize){
            forwardPacket();
        }
        packets[key] = {source,destination, timestamp};
        q.push(key);
        timeStamps[destination].push_back(timestamp);
        return true;
    }
    
    vector<int> forwardPacket() {
        if(q.size() == 0)
        return {};
        long long key = q.front();
        q.pop();
        vector <int> res = packets[key];
        int dest = res[1];
        packets.erase(key);
        
        timeStamps[dest].erase(timeStamps[dest].begin());// vector erase
return res;
    }
    
    int getCount(int destination, int startTime, int endTime) {
        if(timeStamps.find(destination) == timeStamps.end())
        return 0;

        vector <int> &list = timeStamps[destination];
        // find lower bound of startTime and upper bound of end time
        int left = lower_bound(list.begin(),list.end(),startTime) - list.begin();
        int right = upper_bound(list.begin(),list.end(),endTime)-list.begin();
        return right - left;

    }
};

/**
 * Your Router object will be instantiated and called as such:
 * Router* obj = new Router(memoryLimit);
 * bool param_1 = obj->addPacket(source,destination,timestamp);
 * vector<int> param_2 = obj->forwardPacket();
 * int param_3 = obj->getCount(destination,startTime,endTime);
 */