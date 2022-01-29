import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class 최소_최대 {
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
        bw.write(ary[0] + " " + ary[ary.length - 1] +"\n");
        bw.flush();
        bw.close(); 

    }
}
