import java.io.*;

public class 숫자의_합 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int n = Integer.parseInt(br.readLine());
        char[] ary = br.readLine().toCharArray();
        int result = 0;
        for(int i = 0; i < ary.length; i++) {
            result += ary[i] - '0';
        }
        bw.write(Integer.toString(result));
        bw.flush();
        bw.close();
    }
}
