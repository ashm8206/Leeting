class Solution {
    public int[] exclusiveTime(int n, List<String> logs) {

      int[] res = new int[n];
      Stack<int[]> stack = new Stack<>();

      for(String log: logs) {
        String[] logInfo = log.split(":");

        int processId = Integer.parseInt(logInfo[0]); 
        String processStatus = logInfo[1];
        int processTime = Integer.parseInt(logInfo[2]); 
      
        if (processStatus.equals("start")){
            stack.add(new int[]{processId, processTime});
        }
        else {
            // Only top process can end
            // current_process == process_end

            int[] pair = stack.pop();
            int current_process = pair[0];
            int processStart = pair[1];

            int curr_running_time = processTime - processStart + 1;
            res[current_process]+= curr_running_time ;

            if (!stack.empty()) {
                // subtract, current process duration
                // from next item in stack
                int nextInLineProcess = stack.peek()[0];
                res[nextInLineProcess] -= curr_running_time;
              
            }
        }
        

      }

      return res;  
    }
}