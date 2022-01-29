import java.io.*;

public class 빠른AplusB {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        for(int i=0; i < n; i++) {
            String[] ary = br.readLine().split(" ");
            bw.write(Integer.parseInt(ary[0]) + Integer.parseInt(ary[1]) + "\n");
        }
        bw.flush();
        bw.close();
    }
}