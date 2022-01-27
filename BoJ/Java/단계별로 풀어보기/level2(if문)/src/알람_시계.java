import java.io.*;

public class 알람_시계 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] input = br.readLine().split(" ");
        int h = Integer.parseInt(input[0]);
        int m = Integer.parseInt(input[1]);

        int result = h * 60 + m - 45;
        if (result < 0) {
            result = 24 * 60 + result;
        }

        bw.write(result / 60 + " " + result % 60 + "\n");
        bw.flush();
        bw.close();
    }   
}
