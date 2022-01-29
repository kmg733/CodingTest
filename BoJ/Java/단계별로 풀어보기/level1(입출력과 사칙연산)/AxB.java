import java.io.*;

public class AxB {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String input = br.readLine();
        String[] splits = input.split(" ");
        bw.write(Integer.parseInt(splits[0]) * Integer.parseInt(splits[1]) + "\n");
        bw.flush();
        bw.close();
    }
}
