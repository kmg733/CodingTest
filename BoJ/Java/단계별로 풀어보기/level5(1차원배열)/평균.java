import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class 평균 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        String[] str = br.readLine().split(" ");
        int[] ary = new int[str.length];
        for(int i = 0; i < str.length; i++) {
            ary[i] = Integer.parseInt(str[i]);
        }
        Arrays.sort(ary);

        float sum = 0;
        for(int i = 0; i < ary.length; i++) {
            sum += (ary[i] / (float)ary[ary.length-1] * 100); 
        }
        float result = sum / n;
        bw.write(result +"\n");
        bw.flush();
        bw.close(); 

    }
}
