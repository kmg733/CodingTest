import java.util.*;

public class 더_맵게 {
    public static void main(String[] args) {
        int[] scoville = {1, 2, 3, 9, 10, 12};
        int K = 2;
        System.out.println(solution(scoville, K));
    }
    
    public static int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        
        for(int sco : scoville) {
            heap.add(sco);
        }
        
        while(heap.peek() <= K) {
            if(heap.size() == 1) {
                return -1;
            }
            int a = heap.poll();
            int b = heap.poll();
            heap.add(a + b * 2);
            answer++;
        }
        return answer;
    }
}

// 알고리즘 종류
// 힙