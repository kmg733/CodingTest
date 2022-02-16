import java.util.*;

public class 기능개발 {
    public static void main(String[] args) {
        int[] progresses = {95, 90, 99, 99, 80, 99};
        int[] speeds = {1, 1, 1, 1, 1, 1};
        int[] answer = solution1(progresses, speeds);
        for( int i : answer){
            System.out.println(i);
        }
    }

    // Queue(Deque)를 이용한 풀이    
    public static int[] solution2(int[] progresses, int[] speeds) {
        Deque<Integer> q = new LinkedList<>();
        List<Integer> list = new ArrayList<>();
        
        for(int i = 0; i < speeds.length; i++) {
            double remain = (100 - progresses[i]) / (double) speeds[i];
            int day = (int) Math.ceil(remain); 

            if(!q.isEmpty() && q.peek() < day) {
                list.add(q.size());
                q.clear();
            }

            q.offer(day);
        }

        list.add(q.size());
        int[] answer = new int[list.size()];
        for(int i = 0; i < answer.length; i++) {
            answer[i] = list.get(i);
        }

        return answer;
    }

    // ArrayList를 이용한 풀이
    public static int[] solution1(int[] progresses, int[] speeds) {
        List<Integer> list = new ArrayList<>();
        // 작업이 끝날때까지 걸리는 날짜를 저장할 변수
        int[] day = new int[speeds.length];
        
        for(int i = 0; i < speeds.length; i++) {
            day[i] = (100 - progresses[i]) / speeds[i];
            // 나누어 떨어지지 않으면 하루 추가
            if((100 - progresses[i]) % speeds[i] != 0) {
                day[i] += 1;
            }
        }
        
        int prev = day[0];
        int count = 0;
        // 주어지는 prev 변수보다 작은 작업들의 개수를 구함
        for(int i = 0; i < day.length; i++) {
            if( prev < day[i]) {
                list.add(count);
                count = 1;
                prev = day[i];
            } else {
                count++;
            }
        }
        list.add(count);
                
        int[] answer = new int[list.size()];
        for(int i = 0; i < list.size(); i++) {
            answer[i] = list.get(i);
        }
        
        return answer;
    }
}

// 알고리즘 종류
// 스택/큐