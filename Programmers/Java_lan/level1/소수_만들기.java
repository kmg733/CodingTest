import java.util.*;

public class 소수_만들기 {
    public static void main(String[] args) {
        int nums[] = {1, 2, 7, 6, 4};
        System.out.println(solution(nums));
    }

    public static int solution(int[] nums) {
        int answer = 0;

        int sum = 0;
        for(int i = 0; i < nums.length - 2; i++) {
            for(int j = i + 1; j < nums.length - 1; j++) {
                for(int k = j + 1; k < nums.length; k++) {
                    sum = nums[i] + nums[j] + nums[k];
                    if(isDecimal(sum)) {
                        answer++;
                    }
                }
            }
        }

        return answer;
    }

    public static boolean isDecimal(int a) {
        if(a % 2 == 0) {
            return false;
        }
        int num = (int)Math.sqrt(a)+1;

        for(int i = 2; i <= num; i++) {
            if(a % i == 0) {
                return false;
            }
        }
        return true;
    }
}
