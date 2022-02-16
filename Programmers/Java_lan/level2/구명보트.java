import java.util.Arrays;

public class 구명보트 {
    public static void main(String[] args) {
        int[] people = {70, 50, 80, 50};
        System.out.println(solution(people, 100));
    }

    public static int solution(int[] people, int limit) {
        int answer = 0;
        
        Arrays.sort(people);
        int min = 0;
        // 몸무게가 가장 무거운 사람부터 확인
        for(int max = people.length - 1; min <= max; max--) {
            // 최대 + 최소 몸무게 2명의 몸무게 합이 무게 제한보다 낮은경우
            // 최대, 최소 인원을 보트에 태워 보냄
            if(people[min] + people[max] <= limit)
                min++;
            // if문에 안걸리는 경우는 최대 몸무게를 가진 인원만 보트에 태워 보냄
            answer++;
        }
        
        return answer;
    }
}
