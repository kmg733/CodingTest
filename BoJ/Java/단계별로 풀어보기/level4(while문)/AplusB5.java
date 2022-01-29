import java.io.*;

public class AplusB5 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        while(true) {
            String[] ary = br.readLine().split(" ");
            int a = Integer.parseInt(ary[0]);
            int b = Integer.parseInt(ary[1]);
            
            if (a == 0 & b == 0) {
                break;
            }
            bw.write(a + b + "\n");
        }
        bw.flush();
        bw.close();
    }
}
