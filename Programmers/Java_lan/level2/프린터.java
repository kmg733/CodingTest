import java.util.*;

public class 프린터 {
    public static void main(String[] args) {
        int[] priorities = {1, 1, 9, 1, 1, 1};
        int location = 0;
        System.out.println(solution1(priorities, location));
    }

    // 우선순위 큐(PriorityQueue)를 사용한 경우
    public static int solution1(int[] priorities, int location) {
        // 내림차순
        PriorityQueue<Integer> que = new PriorityQueue<>(Collections.reverseOrder());        

        // 우선순위 큐에 값넣기
        for(int n : priorities) {
            que.offer(n);
        }
        int answer = 0;        
        // 큐가 빌 때까지 반복
        while(!que.isEmpty()) {
            for(int i = 0; i < priorities.length; i++) {
                // 큐의 첫 번째 값이 찾는값과 일치하는 경우

                // priorities = [1, 1, 9, 1, 1, 1]
                // que = [9, 1, 1, 1, 1, 1]
                if(que.peek() == priorities[i]) {
                    que.poll();
                    answer++;
                    // 찾는 위치와 일치하는 경우
                    if(location == i)
                        return answer;
                }
            }
        }
        
        return answer;
    }
}

// 알고리즘 종류
// 스택/큐