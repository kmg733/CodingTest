import java.io.*;
import java.util.StringTokenizer;

public class AminusB {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st;
        String input = br.readLine();
        st = new StringTokenizer(input, " ");

        int result = Integer.parseInt(st.nextToken()) - Integer.parseInt(st.nextToken());        

        bw.write(result+"\n");
        bw.flush();
        bw.close();
    }
}
