import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class 숫자의_개수 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int result = 1;
        for(int i = 0; i < 3; i++) {
            result *= Integer.parseInt(br.readLine());
        }
        
        // 자동으로 값을 0으로 초기화
        int[] ary = new int[10];

        String toStr = Integer.toString(result);
        for(int i = 0; i < toStr.length(); i++) {
            ary[toStr.charAt(i) - '0'] += 1;
        }
       
        // 이렇게 풀어도 됨
        // while (result != 0) {
        //     ary[result % 10]++;
        //     result /= 10;
        // }

        for(int i = 0; i < 10; i++) {
            bw.write(ary[i] + "\n");
        }
        
        bw.flush();
        bw.close();
    }
}
