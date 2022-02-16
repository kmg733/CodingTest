import java.util.HashMap;
import java.util.Arrays;
import java.util.Map;
import java.io.*;

public class 전화번호_목록 {
    public static void main(String[] args) throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String[] phone_book = {"123", "456", "789"};
        bw.write(solution2(phone_book) + "\n");
        bw.flush();
        bw.close();
    }

    // sort 이용하는 방법
    public static boolean solution(String[] phone_book) {
        
        // 문자열 정렬
        Arrays.sort(phone_book);

        for(int i = 0; i < phone_book.length - 1; i++) {
            if(phone_book[i + 1].startsWith(phone_book[i])) {
                return false;
            }
        }        

        return true;
    }

    // 해쉬 맵 이용하는 방법
    public static boolean solution2(String[] phone_book) {
        Map<String, Integer> map = new HashMap<>();

        // phone_book[i]를 Key값, i값을 Value로 갖는 HashMap 생성
        for(int i = 0; i < phone_book.length; i++) {
            map.put(phone_book[i], i);
        }

        for(int i = 0; i < phone_book.length; i++) {
            for(int j = 0; j < phone_book[i].length(); j++) {
                if(map.containsKey(phone_book[i].substring(0, j))) {
                    return false;
                }
            }
            
        }

        return true;
    }
}

// 알고리즘 종류
// 해쉬