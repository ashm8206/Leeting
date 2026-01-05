class Solution {
    public int smallestChair(int[][] times, int targetFriend) {
        // int n = times.length;
        // int[][] friends = new int[n][3];

        // for(int i= 0; i < n ; i++){
        //     friends[i] = new int[]{times[i][0], times[i][1], i};
        // }
        // Arrays.sort(friends, (a,b) -> a[0]-b[0]);

        int targetArrival = times[targetFriend][0];
        Arrays.sort(times, (a,b) -> a[0]-b[0]);
        
        PriorityQueue<Integer> unOccupied = new PriorityQueue<>();
        PriorityQueue<int[]> Occupied = new PriorityQueue<>((a,b) -> a[0] -b[0]);
        int nextChair = 0;
        int chair = 0;

        // System.out.println(Arrays.deepToString(friends));
        for(int[] time: times) {

            int arr = time[0], leav = time[1];
            
            while(!Occupied.isEmpty() && Occupied.peek()[0] <= arr){
                chair = Occupied.poll()[1];   
                unOccupied.offer(chair);
            }

            chair  = unOccupied.isEmpty() ? nextChair++ : unOccupied.poll();

            // if (unOccupied.isEmpty()) {
            //     chair = nextChair;
            //     nextChair = chair + 1;
            // }
            // else {
            //     chair = unOccupied.poll();
            // }
            Occupied.offer(new int[] {leav, chair}); 

            if(targetArrival == arr){
                return chair;
            }

        }
        return 0;
    }
}