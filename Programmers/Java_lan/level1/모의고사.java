import java.util.ArrayList;
import java.util.Arrays;

public class 모의고사 {
    public static void main(String[] args) {
        int[] answers = {1,2,3,4,5};
        int[] result = solution(answers);
        for(int i : result) {
            System.out.println(i);
        }
    }
    public static int[] solution(int[] answers) {
        ArrayList<Integer> list = new ArrayList<>();
        int[] ary1 = {1, 2, 3, 4, 5};
        int[] ary2 = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] ary3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};        
 
        int[] score = new int[3];
        for(int i = 0; i < answers.length; i++) {
            if(answers[i] == ary1[i % ary1.length]) {
                score[0] += 1;
            }
            if(answers[i] == ary2[i % ary2.length]) {
                score[1] += 1;
            }
            if(answers[i] == ary3[i % ary3.length]) {
                score[2] += 1;
            }
        }

        int[] temp = new int[score.length];
        for(int i = 0; i < score.length; i++){
            temp[i] = score[i];
        }
        
        Arrays.sort(temp);
        
        for(int i = 0; i < temp.length; i++) {
            if(score[i] == temp[2]) {
                list.add(i + 1);
            }
        }
        
        int[] answer = new int[list.size()];        
        for(int i = 0; i < list.size(); i++) {
            answer[i] = list.get(i);
        }
        return answer;
    }
}
