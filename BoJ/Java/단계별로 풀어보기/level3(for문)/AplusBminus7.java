import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class AplusBminus7 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int t = Integer.parseInt(br.readLine());

        for(int i = 1; i <= t; i++) {
            String[] ary = br.readLine().split(" ");
            int result = Integer.parseInt(ary[0]) + Integer.parseInt(ary[1]);
            bw.write("Case #" + i + ": " + result +"\n");
        }
        bw.flush();
        bw.close();
    }
}
