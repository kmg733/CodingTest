import java.io.*;

public class 윤년 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int input = Integer.parseInt(br.readLine());
        int result = -1;
        if(input % 4 == 0) {
            if(input % 100 != 0 | input % 400 == 0) {                
                result = 1;
            } else {
                result = 0;
            }
        } else {
            result = 0;
        }

        bw.write(result + "\n");
        bw.flush();
        bw.close();
    }
}
