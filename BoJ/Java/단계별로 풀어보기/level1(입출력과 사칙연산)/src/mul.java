import java.io.*;

public class mul {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int A = Integer.parseInt(br.readLine());
        String B = br.readLine();

        // 방법1 - Character.getNumericValue
        bw.write(Character.getNumericValue(B.charAt(2)) * A + "\n");

        // 방법2 - '0'을 빼기
        bw.write((B.charAt(1) - '0') * A + "\n");
        bw.write((B.charAt(0) - '0') * A + "\n");
        bw.write(Integer.parseInt(B) * A + "\n");

        bw.flush();
        bw.close();
    }
}