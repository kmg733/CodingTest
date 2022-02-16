import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class 더하기_사이클 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int input = Integer.parseInt(br.readLine());
        int origin = input;
        int count = 0;
        while(true) {
            int a = input / 10;
            int b = input % 10;
            int c = (a + b) % 10;            
            input = b * 10 + c;
            count += 1;
            if (input == origin) {
                break;
            }
       }
       bw.write(count + "\n");
       bw.flush();
       bw.close(); 

    }
}
