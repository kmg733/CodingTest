import java.util.*;

public class 다리를_지나는_트럭 {
    public static void main(String[] args) {
        int bridge_length = 2;
        int weight = 10;
        int[] truck_weights = {7,4,5,6};
        System.out.println(solution(bridge_length, weight, truck_weights));
    }

    // Deque를 사용한 방법
    public static int solution(int bridge_length, int weight, int[] truck_weights) {
        Deque<Integer> que = new LinkedList<>(); 

        int time = 0;
        int sumWeights = 0;
        
        for(int i = 0; i < truck_weights.length; i++) {            
            while(true) {
                // 큐(다리)가 비어 있다면
                if(que.isEmpty()) {
                    que.add(truck_weights[i]);
                    sumWeights += truck_weights[i];
                    time++;
                    break;       
                
                // 큐(다리)가 꽉차 있을때
                } else if (que.size() == bridge_length) {
                    sumWeights -= que.poll();
                    
                // 큐(다리)에 값이 이미 존재하고, 빈 공간이 있을 때
                } else {
                    // 기존에 다리에 있는 트럭과 추가한 트럭이 최대 중량을 넘지 않을 때
                    if(sumWeights + truck_weights[i] <= weight) {
                        que.add(truck_weights[i]);
                        sumWeights += truck_weights[i];
                        time++;
                        break;
                    // 기존에 다리에 있는 트럭과 추가한 트럭이 최대 중량을 넘을 때
                    } else {
                        que.add(0);
                        time++;
                    }
                }
            }
        }
        return time + bridge_length;
    }
}
