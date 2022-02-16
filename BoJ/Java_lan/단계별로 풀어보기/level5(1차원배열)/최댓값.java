import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class 최댓값 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int index = -1, temp, max = -1;
        for(int i = 0; i < 9; i++) {
            temp = Integer.parseInt(br.readLine());
            if(max < temp) {
                max = temp;
                index = i + 1;
            }
        }
        bw.write(max +"\n");
        bw.write(index +"\n");
        bw.flush();
        bw.close(); 

    }
}
