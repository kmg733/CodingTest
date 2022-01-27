import java.io.*;

public class 두_수_비교하기 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
 
        String[] input = br.readLine().split(" ");
        int A = Integer.parseInt(input[0]);
        int B = Integer.parseInt(input[1]);

        if(A > B) {
            bw.write(">");
        } else if(A < B) {
            bw.write("<");
        } else {
            bw.write("==");
        }

        bw.flush();
        bw.close();
    }
}
