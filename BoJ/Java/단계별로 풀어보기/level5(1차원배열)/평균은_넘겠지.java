import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class 평균은_넘겠지 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int c = Integer.parseInt(br.readLine());

        for(int i = 0; i < c; i++) {
            String[] str = br.readLine().split(" ");
            int[] ary = new int[str.length];
            for(int j = 0; j < str.length; j++) {
                ary[j] = Integer.parseInt(str[j]);
            }

            int sum = 0;
            for(int j = 1; j < ary.length; j++) {
                sum += ary[j];
            }
            float avg = sum / ary[0];

            int overAvg = 0;
            for(int j = 1; j < ary.length; j++) {
                if(ary[j] > avg) {
                    overAvg += 1;
                }
            }       
            double student = overAvg / (double)ary[0] * 100;
            bw.write(String.format("%.3f", student) +"%\n");
        }       
        bw.flush();
        bw.close(); 
    }
}
