import java.io.*;

public class 문자열_반복 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int t = Integer.parseInt(br.readLine());

        for(int i = 0; i < t; i++) {
            String[] cases = br.readLine().split(" ");
            int mul = Integer.parseInt(cases[0]);
            char[] strs = cases[1].toCharArray();
            for(int j = 0; j < strs.length; j++) {
                for(int k = 0; k < mul; k++) {
                    sb.append(strs[j]);
                }
            }
            sb.append("\n");
        }

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}
