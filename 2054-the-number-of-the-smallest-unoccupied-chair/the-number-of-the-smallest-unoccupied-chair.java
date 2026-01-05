class Solution {
    public int smallestChair(int[][] times, int targetFriend) {
        int n = times.length;
        int[][] friends = new int[n][3];

        for(int i= 0; i < n ; i++){
            friends[i] = new int[]{times[i][0], times[i][1], i};
        }
        Arrays.sort(friends, (a,b) -> Integer.compare(a[0],b[0]));
        
        PriorityQueue<Integer> unOccupied = new PriorityQueue<>();
        PriorityQueue<int[]> Occupied = new PriorityQueue<>((a,b) -> Integer.compare(a[0], b[0]));
        int nextChair = 0;
        int chair = 0;

        // System.out.println(Arrays.deepToString(friends));
        for(int i = 0; i < n ; i++) {

            int arr = friends[i][0], leav = friends[i][1], friend = friends[i][2];
            
            while(!Occupied.isEmpty() && Occupied.peek()[0] <= arr){
                int[] top = Occupied.poll();   
                chair = top[1];
                unOccupied.offer(chair);
            }

            if (unOccupied.isEmpty()) {
                chair = nextChair;
                nextChair = chair + 1;
            }
            else {
                chair = unOccupied.poll();
            }
            Occupied.offer(new int[] {leav, chair}); 
            
            System.out.println(friend + " " + chair);
            if(targetFriend == friend){
                return chair;
            }

        }
        return 0;
    }
}