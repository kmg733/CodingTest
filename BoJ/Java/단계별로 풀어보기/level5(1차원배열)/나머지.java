import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class 나머지 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int[] ary = new int[42];
        for(int i = 0; i < 10; i++) {
            ary[Integer.parseInt(br.readLine()) % 42] += 1;
        }
        
        int count = 0;
        for(int i = 0; i < ary.length; i++) {
            if(ary[i] == 0) {
                continue;
            } else {
                count += 1;
            }
        }
        bw.write(count + "\n");
        bw.flush();
        bw.close();
    }
}
