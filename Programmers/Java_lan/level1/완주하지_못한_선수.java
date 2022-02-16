import java.util.Arrays;

class 완주하지_못한_선수 {
    public static void main(String[] args) {
        
        String[] participant = {"leo", "kiki", "eden"};
        String[] completion = {"eden", "kiki"};
        완주하지_못한_선수 so = new 완주하지_못한_선수();
        System.out.println(so.solution(participant, completion));
        
    }
    public String solution(String[] participant, String[] completion) {
        Arrays.sort(participant);
        Arrays.sort(completion);
    
        int idx = participant.length - 1;

        for(int i = 0; i < completion.length; i++) {
            if(!participant[i].equals(completion[i])) {
                idx = i;
                break;
            }
        }
        String answer = participant[idx];
        return answer;
    }
}