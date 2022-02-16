import java.util.*;

public class 주식가격 {
    public static void main(String[] args) {
        int[] prices = {1, 2, 3, 2, 3};
        int[] answers = solution2(prices);
        for (int answer : answers) {
            System.out.println(answer);
        }
    }

    // 2중 for문으로 푸는 방법
    public static int[] solution1(int[] prices) {
        int[] answer = new int[prices.length];
        
        for(int i = 0; i < prices.length; i++) {            
            for(int j = i + 1; j < prices.length; j++) {     
                answer[i]++;
                if(prices[i] > prices[j]) {
                    break;
                }
            }
        }

        return answer;
    }

    // Stack을 사용하여 푸는 방법
    public static int[] solution2(int[] prices) {
        int[] answer = new int[prices.length];
        Deque<Integer> stk = new LinkedList<>();
        
        for(int i = 0; i < prices.length; i++) {      
            // 주식이 감소하는 시점 찾기      
            while(!stk.isEmpty() && prices[i] < prices[stk.peek()]) {
                answer[stk.peek()] = i - stk.peek();
                stk.pop();
            }
            stk.push(i);
        }
        while(!stk.isEmpty()) {
            answer[stk.peek()] = prices.length - stk.peek() - 1;
            stk.pop();
        }

        return answer;
    }
}

// 알고리즘 종류
// 스택/큐