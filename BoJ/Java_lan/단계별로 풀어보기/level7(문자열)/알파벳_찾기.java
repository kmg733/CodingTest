import java.io.*;

public class 알파벳_찾기 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringBuilder sb = new StringBuilder();

        String str = br.readLine();
        int start = (int)'a';
        int end =  (int)'z';
        for(int i = start; i <= end; i++) {
            sb.append(str.indexOf((char)i) + " ");
        }

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}
