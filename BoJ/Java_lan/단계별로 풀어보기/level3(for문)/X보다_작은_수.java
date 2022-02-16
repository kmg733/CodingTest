import java.io.*;

public class X보다_작은_수 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        String[] ary = br.readLine().split(" ");
        int n = Integer.parseInt(ary[0]);
        int x = Integer.parseInt(ary[1]);

        String[] input =  br.readLine().split(" ");
        for(int i = 0; i < n; i++) {
            if(Integer.parseInt(input[i]) < x) {
                sb.append(input[i] + " ");
            }
        }
        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}
