import java.util.*;

public class 가장_큰_수 {
    public static void main(String[] args) {
        int[] numbers = {3, 30, 34, 5, 9};
        System.out.println(solution(numbers));
    }
    public static String solution(int[] numbers) {

        String[] str = new String[numbers.length];        
        for(int i = 0; i < str.length; i++) {
            str[i] = String.valueOf(numbers[i]);
        }
        
        Arrays.sort(str, new Comparator<String>() {
           public int compare(String o1, String o2) {
               return (o2 + o1).compareTo(o1 + o2);
           } 
        });
        
        if(str[0].equals("0"))
            return "0";
        
        return String.join("", str);
    }
}
