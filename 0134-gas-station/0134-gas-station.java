class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {   

        // gas - cost 를구한다
        int n = gas.length;
        int[] diff = new int[n];
        for(int i = 0; i < n; i++) {
            diff[i] = gas[i] - cost[i];
        }
        
        
        if (Arrays.stream(diff).sum() < 0 ) {
            return -1;
        }
        
        
        // for문 한번으로 해결해보자.
        int fuel = 0;
        int start = 0;
        for(int i = 0; i < n; i++) {
            if ((fuel + diff[i]) < 0) {
                fuel = 0;
                start = i + 1;
            } else {
                fuel += diff[i];
            }

        }
        
        return start;
    }
}



/*
1 2 3 4 5  - gas
3 4 5 1 2  - cost
-2 -2 -2 3 3
*/