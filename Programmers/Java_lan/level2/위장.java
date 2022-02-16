import java.util.HashMap;

public class 위장 {
    public static void main(String[] args) {
        String[][] clothes = {{"yellowhat", "headgear"}, {"bluesunglasses", "eyewear"}, {"green_turban", "headgear"}};
        System.out.println(solution(clothes));
    }

    public static int solution(String[][] clothes) {
        HashMap<String, Integer> map = new HashMap<>();
        for(String[] cloth : clothes) {
            // getOrDefault는 찾는 키가 존재한다면 찾는 키의 값을 반환하고 없다면 기본 값을 반환하는 메서드
            // 모두 입지 않는 경우도 하나 있기 때문에 시작값을 1로둠
            map.put(cloth[1], map.getOrDefault(cloth[1], 1) + 1);
        }
        
        int answer = 1;
        // 키값을 하나씩 불러서 경우의 수 계산을 위해 곱함
        for(String key : map.keySet()) {
            answer *= map.get(key);
        }
        return answer - 1;
    }
}

// 알고리즘 종류
// 해쉬