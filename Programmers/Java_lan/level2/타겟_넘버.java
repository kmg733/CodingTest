public class 타겟_넘버 {
    static int answer = 0;
    
    public static void main(String[] args) {
        int[] numbers = {1, 1, 1, 1, 1};
        System.out.println(solution(numbers, 3));
    }

    public static int solution(int[] numbers, int target) {
        dfs(numbers, 0, target, 0);
        return answer;
    }
    
    public static void dfs(int[] numbers, int idx, int target, int sum) {
        if(idx == numbers.length) {
            if(sum == target){
                answer++;                
            }
        } else {
            dfs(numbers, idx + 1, target, sum + numbers[idx]);
            dfs(numbers, idx + 1, target, sum - numbers[idx]);            
        }
        
    }
}
