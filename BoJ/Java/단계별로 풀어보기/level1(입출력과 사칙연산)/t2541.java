import java.io.*;

public class t2541 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int input = Integer.parseInt(br.readLine());
        bw.write(input-543 + "\n");
        bw.flush();
        bw.close();
    }
}
