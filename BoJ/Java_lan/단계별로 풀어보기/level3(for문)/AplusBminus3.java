import java.io.*;

public class AplusBminus3 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int t = Integer.parseInt(br.readLine());
        for(int i = 0; i < t; i++) {
            String[] AandB = br.readLine().split(" ");
            bw.write(Integer.parseInt(AandB[0]) + Integer.parseInt(AandB[1])+ "\n");
        }
        bw.flush();
        bw.close();
    }
}